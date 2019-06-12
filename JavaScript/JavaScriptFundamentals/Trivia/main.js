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
    // Each Category should have 3 questions. one each easy, medium and hard 


    
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
    
    var $categoryOne = $('cat1')
    
    // Technical experience
    // New Questions
    // -> 3 random categories selected
    // -> 9 Ajax requests for 3 categories with 3 questions each of varying difficulty
    // -> Create hidden p tag
    // -> Question selected
    // -> update HTML in this question i.e id=cat2-q2
    // -> 
    
    $.ajax({
        url: "https://opentdb.com/api.php?\
            amount=3&\
            category=21&\
            difficulty=easy&\
            type=multiple",
        success: function(data) {
            $.each(data.results, function(i, result) {

            })
        }
    })






});
