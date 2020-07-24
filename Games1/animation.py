import pyglet

animated_background = pyglet.image.load_animation('Games1/images/spacegif.gif')
animation_sprites = pyglet.sprite.Sprite(animated_background)
w = animation_sprites.width
h = animation_sprites.height
window = pyglet.window.Window(width=w, height=h)
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pyglet.gl.glClearColor(r, g, b, alpha)


@window.event
def on_draw():
    window.clear()
    animation_sprites.draw()


pyglet.app.run()
