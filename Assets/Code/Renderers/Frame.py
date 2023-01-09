

def draw(ctx, me):
    styleImage = ctx.getStyleImage(me['style'])
    srcW = ctx.window.getImageWidth(styleImage)
    srcH = ctx.window.getImageHeight(styleImage)

    # extract the frame's parameters for convenience
    styleData = ctx.getStyleData(me['style'])
    th = styleData['th']
    lw = styleData['lw']
    bh = styleData['bh']
    rw = styleData['rw']

    dr = me['drawRect']

    # Compute the sizes of the 'stretchy' bits
    srcRW = srcW - (lw + rw)
    srcRH = srcH - (lw + rw)
    dstRW = dr.w - (lw + rw)
    dstRH = dr.h - (th + bh)

    # Top...
    if th > 0:
        if lw > 0:   # Left
            ctx.window.drawImage(0, 0, lw, th, styleImage, dr.x, dr.y, lw, th)
        if srcRW > 0:   # Middle...stretches as needed
            ctx.window.drawImage(lw, 0, srcRW, th, styleImage, dr.x + lw, dr.y, dstRW, th)
        if rw > 0:   # Right
            ctx.window.drawImage(srcW - rw, 0, rw, th, styleImage, (dr.x + dr.w) - rw, dr.y, rw, th)

    # Middle...
    if srcRH > 0:
        if lw > 0:   # Left
            ctx.window.drawImage(0, th, lw, srcRH, styleImage, dr.x, dr.y + th, lw, dstRH)
        if srcRH > 0:   # Middle...stretches as needed
            ctx.window.drawImage(lw, th, srcRW, srcRH, styleImage, dr.x + lw, dr.y + th, dstRW, dstRH)
        if rw > 0:   # Left
            ctx.window.drawImage(srcW - rw, th, rw, srcRH, styleImage, (dr.x + dr.w) - rw, dr.y + th, rw, dstRH)

    # Bottom...
    if bh > 0:
        if lw > 0:   # Left
            ctx.window.drawImage(0, srcH - bh, lw, bh, styleImage, dr.x, (dr.y + dr.h) - bh, lw, bh)
        if srcRW > 0:   # Middle...stretches as needed
            ctx.window.drawImage(lw, srcH - bh, srcRW, bh, styleImage, dr.x + lw, (dr.y + dr.h) - bh, dstRW, bh)
        if rw > 0:   # Right
            ctx.window.drawImage(srcW - rw, srcH - bh, rw, bh, styleImage, (dr.x + dr.w) - rw, (dr.y + dr.h) - bh, rw, bh)

    # ctx.window.drawImage(0,0, srcW, srcH, styleElement, dr.x, dr.y, dr.w, dr.h)
