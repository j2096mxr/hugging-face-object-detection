import transformers
from PIL import Image
from PIL import ImageDraw


img = Image.open('crash1.jpg')

model = transformers.pipeline('object-detection')

result = model(img)

th: any

draw = ImageDraw.Draw(img)

for instance in result:
    score = instance['score']

    if score < th:
        continue

    label = instance['label']
    box = instance['box']
    x1 = box['xmin']
    y1 = box['ymin']
    x2 = box['xmax']
    y2 = box['ymax']
    width = x2-x1
    height = y2 - y1

    print(f'{label} -> score: {score}, ({x1}, {y1})-({x2}, {y2}) {width}x{height}')

    draw.rectangle( ( (x1, y1), (x2, y2)), width = 2, outline = 'RED')

    draw.text( ( x1, y1), f'{label} {score*100:.lf}%', font_size=10)

img.show()
