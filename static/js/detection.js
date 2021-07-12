import * as cocoSsd from "@tensorflow-models/coco-ssd";

const image = document.getElementById("image")

cocoSsd.load()
  .then(model => model.detect(image))
  .then(predictions => console.log(predictions))

