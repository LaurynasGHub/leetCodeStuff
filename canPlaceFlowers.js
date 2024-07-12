function canPlaceFlowers (flowerbed, n) {
    let plantPlaces = 0;

    if (flowerbed.length >= 2) {
        for (i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                if (i > 0){
                    if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0) {
                        flowerbed[i] = 1;
                        plantPlaces++;
                    };
                }else{
                    if(flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        plantPlaces++;
                    };
                };
                if (i == (flowerbed.length-1)){
                    if (flowerbed[i - 1] == 0) {
                        flowerbed[i] = 1;
                        plantPlaces++;
                    };
                };
            };
        };
    }else{
        flowerbed[0] == 1 ? plantPlaces = 0 : plantPlaces = 1;
    };

    if (plantPlaces >= n) {
        return true
    } else {
        return false
    }
};
