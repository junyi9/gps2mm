# gps2mm

## Overview
`gps2mm` is a tool designed to transform a given GPS coordinate (latitude and longitude) into the corresponding estimated mile marker along the I-24 highway. 

## Features
- **GPS to Mile Marker Conversion:** Convert GPS coordinates (latitude, longitude) into an estimated mile marker along I-24.

## How it Works
- Given a GPS point, calculate the distance between all the pre-calculated points and find the closest one from that. It can give a estimated mile marker on the road.

See the `demo.ipynb` for a tutorial on how to use the function `gps2mm`.

## Reference
This tool is based on the data developed by Matt et al. (2024) (https://github.com/MatthewNice/gps2vsl) for GPS-based mile marker estimation. Consider cite the following work from Matthew Nice.

**MiddleWay control**:
    @inproceedings{nice2024middle, 
    title={A middle way to traffic enlightenment}, 
    author={Nice, Matthew W and Gunter, George and Ji, Junyi and Zhang, Yuhang and Bunting, Matthew and Barbour, Will and Sprinkle, Jonathan and Work, Daniel B}, 
    booktitle={2024 ACM/IEEE 15th International Conference on Cyber-Physical Systems (ICCPS)}, 
    pages={147--156}, 
    year={2024}, 
    organization={IEEE} 
    }

**vsl-following**
    @article{nice2023sailing, 
    title={Sailing cavs: Speed-adaptive infrastructure-linked connected and automated vehicles}, 
    author={Nice, Matthew and Bunting, Matthew and Gunter, George and Barbour, William and Sprinkle, Jonathan and Work, Dan}, 
    journal={arXiv preprint arXiv:2310.06931}, 
    year={2023} 
    }