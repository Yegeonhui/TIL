from datetime import datetime
now = datetime.today()
def coco_foam():
    foam = {
                "info": {
                        "description": "COCO Dataset",
                        "url": "",
                        "version": "1.0",
                        "year": 2022,
                        "contributor": "IREM",
                        "date_created": datetime.now().strftime('%Y-%m-%d')
                        },

                "licenses": [
                                {
                                    "url": "",
                                    "id": 0,
                                    "name": ""
                                }
                            ],

                "images": [
                            {
                                "license": 0,
                                "file_name": "",
                                "coco_url": "",
                                "height": 0,
                                "width": 0, 
                                "date_captured": "",
                                "flickr_url": "",
                                "id": 0
                            }
                            ],   
                
                "annotations": [  
                                {
                                    "segmentation": [
                                        [
                                        ]
                                    ],
                                    "area": 0,
                                    "iscrowd": 0,
                                    "image_id": 0,
                                    "bbox": [
                                        
                                    ],
                                    "category_id": 0,
                                    "id": 0
                                }
                                ],
                "categories": [
                                {
                                    "supercategory": "",
                                    "id": 0,
                                    "name": ""
                                },
                                ]
                }
    return foam