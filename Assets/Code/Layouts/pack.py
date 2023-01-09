import copy


def layout(ctx, available, me):
    if 'contents' not in me:
        return available   # No-op

    me['drawRect'] = copy.copy(available)

    # reserve the are we need for our style frame
    totalWidth = 0
    maxHeight = 0

    # reserve space now to get positioning correct
    kidAvailable = ctx.adjustAvailableForStyle(me, available)
    for kid in me['contents']:
        kidAvailable = ctx.layout(kidAvailable, kid)
        totalWidth += kid['drawRect'].w
        maxHeight = max(maxHeight, kid['drawRect'].h)

    me['drawRect'].w = totalWidth
    me['drawRect'].h = maxHeight
    ctx.inflateDrawRectForStyle(me)

    available.x += me['drawRect'].w
    available.w -= me['drawRect'].w

    return available
