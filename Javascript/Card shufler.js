//empty deck that can be added onto
const DECK=[];
// all the suits in a standered deck
const SUIT=["H","D","S","C"];
// all the values in a standard deck
const VALUES=["1","2","3","4","5","6","7","8","9","10","11","12","13"];
//a second deck to use after shuffled
const DECK2=[];
// stores the players
const PLAYERS=[];


//presents the code in an organized manner
function main(){
    var players = readInt("How many players? ");
    var cards = readInt("How many cards? ");
   deck();
   shuffle();
   dealCards(players,cards);
   displayHands();
}


    
//List for the suit, list for the value numbers, this function combines these to create a deck
function deck(){
    //rotates through the suit
    for (var i=0; i<SUIT.length; i++){
        //rotates through the values
        for (var j=0; j<VALUES.length; j++){
            //combines the current suit with all values and then oushes them to the deck list
            DECK.push(VALUES[j]+SUIT[i])
        }
    }
}
//shuffles the deck
function shuffle(){
    // does the function bellow until the first deck is empty
    for (var k=0; k<52; k++){
        //finds a random index from the first deck
        var rand = Math.floor(Math.random()*DECK.length);
        // pushes that random index into the second deck
        DECK2.push(DECK[rand]);
        DECK.splice(rand ,1);
    }
}

//deals cards to players
function dealCards(num,cards){
    //stores the number of cards
    var numCards = cards;
    // stores the number of players
    var numPlayers = num;
    //rotates through the players
    for (var i=0; i<numPlayers; i++){
        // creates a list for each player
        const LIST =[];
            // deals the appropriate amounts of cards to each player
        for (var j=0; j<numCards; j++){
            // random card from suffled deck
            var rand = Math.floor(Math.random()*DECK2.length);
            //pushes the random card into the players cards
            LIST.push(DECK2[rand]);
            //removes the card from the shuffled deck
            DECK2.splice(rand,1);
        }
        // moves the players cards into the players list
        PLAYERS.push(LIST);
    }
}

//displays the player's cards
function displayHands(){
    //rotates through number 1- the length of the list of the players
    for (var i=1; i<PLAYERS.length+1; i++){
        // prints out the player number using i and the player's cards using player at ir-1
        console.log("Player " + i + ":" + PLAYERS[i-1])
    }
}

main();