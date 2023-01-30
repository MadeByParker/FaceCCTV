import assets from "./assets";

const cardText = [
      {
            id: 1,
            name: "Home",
            displayName: "FaceCCTV",
            description: "Upload a photo to allow the app to detect faces and enhance the image.",
            image: assets.complete,
      },
      {
            id: 2,
            name: "FaceDetection",
            displayName: "Face Detection",
            description: "Upload a photo to allow the app to detect faces only.",
            image: assets.detected,
      },
      {
            id: 3,
            name: "ImageEnhancement",
            displayName: "Image Enhancement",
            description: "Upload a photo to allow the app to enhance the image.",
            image: assets.plain,
      },
]

export { cardText }