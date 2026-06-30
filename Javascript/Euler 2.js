function main(){
	var a=1;
    var	b=2;
    var total=0;
    console.log(a);
    console.log(b);
    while (true){
        a=a+b;
        if (a>4000000){
            break;
        }
        if (a%2==0){
            total=total+a
        }
        console.log(a)
        b=a+b;
        if (b%2==0){
            total=total+b;
        }
        if (b>4000000){
            break;
        }
        console.log(b);
    }
    console.log(total+2);
    
}

main();