const primes =[2];

function main(){
    var numPrimes=1;
    var num=3;
    while (numPrimes<10010){
        if (isPrime(num)==true){
            numPrimes++
        }
        num +=2
    }
    console.log(primes[10009]);
}

function isPrime(num){
	var truee=true;
    var y=num;
	for (var j=3; j<=Math.sqrt(y); j = j+2){
        if (y%j==0){
            truee=false;
    	    break;
        }
    }
    if(truee==true){
        primes.push(y);
    }
    return truee;
}


main();