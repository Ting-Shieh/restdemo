from aframe_app import app
from aframe_app.views.aframe_views import AFrameViews
from aframe_app.views.blog_views import BlogViews



@app.route('/', methods=['GET'])
def blog_index():
    return BlogViews.index()


# ------------------------------------------------------
# 測試 AFrame
# ------------------------------------------------------

@app.route('/aframe01', methods=['GET'])
def aframe01():
    return AFrameViews.aframe01()

@app.route('/aframe02', methods=['GET'])
def aframe02():
    return AFrameViews.aframe02()



# @app.route('/')
# def index():
#     htmlpage = """
#             <!DOCTYPE html>
#             <html lang="en">
#             <head>
#                 <meta charset="UTF-8">
#                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
#                 <title>Ting's AR-01</title>
#                 <script src="https://aframe.io/releases/0.9.0/aframe.min.js"></script>
#                 <script src="https://rawgit.com/jeromeetienne/ar.js/master/aframe/build/aframe-ar.js"></script>
#                 <script>THREEx.ArToolkitContext.baseURL = 'https://rawgit.com/jeromeetienne/ar.js/master/three.js/'</script>
#             </head>
#             <body style='margin : 0px; overflow: hidden;'>
#
#                 <a-scene embedded arjs='sourceType: webcam; debugUIEnabled: false;'>
#                     <a-marker type='pattern' url='./res/maker.patt'>
#                         <a-entity position='-3 2 0' text="width: 5; value:This is test"></a-entity>
#                         <a-entity position='0 0 0' gltf-model='url(res/scene.gltf)'></a-entity>
#                     </a-marker>
#                     <a-entity camera></a-entity>
#                 </a-scene>
#             </body>
#             </html>
#     """
#
#     return htmlpage


if __name__ == '__main__':
    app.run()
