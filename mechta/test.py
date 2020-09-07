source_dict =   {"additional_image": [
    {
      "url": "/export/1cbitrix/import_files/45/455bf69d-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf69e-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf69f-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf6a0-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf6a1-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf6a2-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    },
    {
      "url": "/export/1cbitrix/import_files/45/455bf6a3-f046-11e7-80cb-1866daf08915.jpeg",
      "alt": "Радиостанции MOTOROLA TLKR T92 H2O"
    }
  ]}

target = '$'.join([item['url'] for item in source_dict['additional_images']]) if 'additional_images' in  source_dict else ''
print(target)