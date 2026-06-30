const palindromes = [];

function main(){
    for (var i = 100; i < 1000; i++){
        for (var j = 100; j < 1000; j++){
            var product = i * j;
            if (isPalindrome(product)) {
                palindromes.push(product);
            }
        }
    }
    console.log("All palindromic products:", palindromes);
    console.log("Largest palindrome:", Math.max(...palindromes));
}

function isPalindrome(x){
    const str = x.toString();
    const reversedStr = str.split('').reverse().join('');
    return str === reversedStr;
}

main();
