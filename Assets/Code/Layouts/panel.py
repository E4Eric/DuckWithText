import copy


def layout(ctx, available, me):
    pct = me['percentage'] / 100
    side = me['side']

    # first layout on top
    me['drawRect'] = copy.copy(available)
    if side == 'top':
        height = int(available.h * pct + 0.5)
        me['drawRect'].h = height

    if side == 'bottom':
        height = int(available.h * pct + 0.5)
        me['drawRect'].y = available.y + height
        me['drawRect'].h = height

    # drawRect set...layout the kids inside me
    # grab room for the style first since we layout inside us...
    kidAvailable = ctx.adjustAvailableForStyle(me, me['drawRect'])
    if 'contents' in me:
        for kid in me['contents']:
            kidAvailable = ctx.layout(kidAvailable, kid)

    # Now if it's on the bottom shift it there
    if side == 'top':
        available.y += height

    if side == 'bottom':
        available.y = available.y + available.h - height
        newY = available.y
        ctx.setModelElementPos(me, me['drawRect'].x, newY)

    available.h -= height

    return available
