function main(){
    var total=0;
    for (var i=0; i<334; i++){
        let num= 3*i;
        console.log(num);
        total= total +num
    }
    for (var i=0; i<200; i++){
        let num= 5*i;
        console.log(num);
        total= total +num
    }
    for (var i=0; i<67; i++){
        let num= 15*i;
        console.log(num);
        total= total -num
    }
    console.log(total);
}
main();