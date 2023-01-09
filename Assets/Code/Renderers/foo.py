

def draw(ctx, me):
    print('draw label: ', me['label'])
    sd = ctx.getStyleData(me['style'])

    # Adjust the top/right for the style
    x = me['drawRect'].x + sd['lw'] + sd['rm']
    y = me['drawRect'].y + sd['th'] + sd['tm']
    text = me['label']

    ctx.window.drawText(x, y, text, '')

