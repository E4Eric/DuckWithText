import copy


def layout(ctx, available, me):
    dr = copy.copy(available)
    # Hack!! assume horizontal, no icon and a three pixel 'gap'

    iconW = 0
    iconH = 0
    if 'icon' in me:
        icon = ctx.getIcon(me['icon'])
        iconW = ctx.window.getImageWidth(icon)
        iconH = ctx.window.getImageHeight(icon)

    textW = 0
    textH = 0
    if 'label' in me:
        textW = ctx.window.getTextWidth(me['label'], me['fontSpec'])
        textH = ctx.window.getTextHeight(me['label'], me['fontSpec'])

    # hack! assume no icon
    dr.w = textW
    dr.h = max(0, textH)
    me['drawRect'] = dr

    ctx.inflateDrawRectForStyle(me)
    available.x += me['drawRect'].w
    available.w -= me['drawRect'].w

    return available
