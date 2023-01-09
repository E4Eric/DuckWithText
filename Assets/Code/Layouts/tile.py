import copy


def layout(ctx, available, me):
    if 'contents' not in me:
        return available   # No-op

    me['drawRect'] = copy.copy(available)
    adjusted = ctx.adjustAvailableForStyle(me, available)
    side = me['side']

    # reserve the are we need for our style frame
    maxHeight = 0

    if side == 'top' or side == 'bottom':
        # reserve space now to get positioning correct
        kidAvailable = copy.copy(adjusted)
        totalHeight = 0
        startWidth = kidAvailable.w
        startX = kidAvailable.x
        for kid in me['contents']:
            kidAvailable = ctx.layout(kidAvailable, kid)
            if kidAvailable.w < 0:  # Ooops...overflow, wrap
                kidAvailable.x = startX
                kidAvailable.w = startWidth
                kidAvailable.y += maxHeight
                kidAvailable.h -= maxHeight
                kidAvailable = ctx.layout(kidAvailable, kid)
                totalHeight += maxHeight
                maxHeight = kid['drawRect'].h

            maxHeight = max(maxHeight, kid['drawRect'].h)

        totalHeight += maxHeight

        # here we need to only change the height for the style
        styleData = ctx.getStyleData(me['style'])
        totalHeight += styleData['th'] + styleData['tm'] + styleData['bh'] + styleData['bm']
        me['drawRect'].h = totalHeight

    if side == 'top':
        available.y += me['drawRect'].h
    elif side == 'bottom':
        dy = available.h - me['drawRect'].h
        ctx.offsetModelElement(me, 0, dy)

    available.h -= me['drawRect'].h

    return available
