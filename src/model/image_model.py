class ImageModel:
    def __init__(self, imageId, imageName, imageWidth, imageHeight, imageType, imagePath, imagePathFinal, imageStatus="pending"):
        self.imageId = imageId
        self.imageName = imageName
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageType = imageType
        self.imagePath = imagePath
        self.imagePathFinal = imagePathFinal
        self.imageStatus = imageStatus

    def to_dict(self):
        return {
            "imageId": self.imageId,
            "imageName": self.imageName,
            "imageWidth": self.imageWidth,
            "imageHeight": self.imageHeight,
            "imageType": self.imageType,
            "imagePath": self.imagePath,
            "imagePathFinal": self.imagePathFinal,
            "imageStatus": self.imageStatus
        }