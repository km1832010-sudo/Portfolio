const primeFactors=[]
const bigNumber =123456789012345678901234567890 ;
function main(){
    for (var i=3; i<bigNumber**0.5; i = i+2){
        if (bigNumber%i==0){
            var x = bigNumber/i;
            isPrime(x);
            isPrime(i);
  	    }
	}
  console.log(primeFactors);
}
function isPrime(num){
	var truee=true;
    var y=num;
    if (y%2==0){
  	    truee=false;
    }else{
	    for (var j=3; j<(y**0.5); j = j+2){
            if (y%j==0 || primeFactors.includes(y)){
                truee=false;
    	        break;
            }
        }
    	if(truee==true){
    	    console.log("true prime = "+ y);
        primeFactors.push(y);
        }
        return truee;
    }
}		

main();