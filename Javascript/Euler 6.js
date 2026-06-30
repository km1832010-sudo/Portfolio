function main(){
    var sums=0;
    var squareSums =0;
    var difference=0;
    for (var i=1; i<101; i++){
        sums= sums+(i**2)
    }
    for (var j=1; j<101; j++){
        squareSums= squareSums+j
    }
    difference = (squareSums**2)-sums
    console.log(difference);
}

main();