$(function() {
    
    const categories = {
        10 : "Entertainment: Books",
        11 : "Entertainment: Film",
        12 : "Entertainment: Music",
        13 : "Entertainment: Musicals & Theatres",
        14 : "Entertainment: Television",
        15 : "Entertainment: Video Games",
        16 : "Entertainment: Board Games",
        17 : "Science & Nature",
        18 : "Science: Computers",
        19 : "Science: Mathematics",
        20 : "Mythology",
        21 : "Sports",
        22 : "Geography",
        23 : "History",
        24 : "Politics",
        25 : "Art",
        26 : "Celebrities",
        27 : "Animals",
        28 : "Vehicles",
        29 : "Entertainment: Comics",
        30 : "Science: Gadgets",
        31 : "Entertainment: Japanese Anime & Manga",
        32 : "Entertainment: Cartoon & Animations",
    };

    


    // TODO
    // Generate three categories
    // Each Category should have 3 questions. one each of: easy, medium and hard 

    
    // 
    // User Experience:
    // New Questions
    // Hide new questions buttons 
    // -> click question-box
    // -> make all other question-boxes unclickable
    // -> shows question / answers for this question-box
    // -> click answer
    // -> if correct, add points, give 'correct' message, delay, gray box
    // -> if incorrect, give 'incorrect' message, delay, gray box
    // -> repeat until all questions answered
    // -> show new questions button
    
    
    // Technical experience
    // New Questions
    // -> 3 random categories selected
    // -> 9 Ajax requests for 3 categories with 3 questions each of varying difficulty
    // -> Create hidden p tag
    // -> Question selected
    // -> update HTML in this question i.e id=cat2-q2
    // -> 
    var $categoryOne = document.getElementById('cat1');
    var $categoryTwo = document.getElementById('cat2');
    var $categoryThree = document.getElementById('cat3');

    function threeCategories() {
        var limit = 3,
            lower_bound = 10,
            upper_bound = 33,
            unique_random_numbers = [];

        while (unique_random_numbers.length < limit) {
            var random_number = Math.floor(Math.random()*(upper_bound - lower_bound) + lower_bound);
            if (unique_random_numbers.indexOf(random_number) == -1) { 
                unique_random_numbers.push( random_number );
            }
        }
        return unique_random_numbers;
    }

    var currentCategories = threeCategories();
    var difficulties = [
        'easy',
        'medium',
        'hard'
    ]

        
    for (var i=1;i<currentCategories.length+1;i++){
        for (var j=1;j<difficulties.length+1;j++){
            $.ajax({
                url: "https://opentdb.com/api.php?\
                    amount=1&\
                    category=" + currentCategories[i] + "&\
                    difficulty=" + difficulties[j] + "&\
                    type=multiple",
                success: function(data) {
                    var $questionDiv = "cat" + i + "-q" + j;
                    var $thisQuestion = document.getElementById($questionDiv);
                    console.log($questionDiv);
                    console.log($thisQuestion);
                }
            })
        }
    }






});
