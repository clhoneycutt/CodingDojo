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
    // -> question-box clicked
    // -> points div selected
    // -> question div selected
    // -> question div searched for category and question
    // -> points variable created
    // -> ajax call created / sent
    // -> points div hidden, questions div unhidden
    // -> 
    
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
    
    // Generate 3 categories and set the category names

    const setCategoryNames = () => {
        var currentCategories = threeCategories();
        
        let [categoryOne, categoryTwo, categoryThree] = currentCategories;
        
        let $categoryOne = document.getElementById('cat1-name');
        let $categoryTwo = document.getElementById('cat2-name');
        let $categoryThree = document.getElementById('cat3-name');
        
        // $categoryOne.innerHTML = categories[categoryOne]
        // $categoryTwo.innerHTML = categories[categoryTwo]
        // $categoryThree.innerHTML = categories[categoryThree]

        return currentCategories;
    }
    

    let currentCategories = setCategoryNames();
    let [categoryOne, categoryTwo, categoryThree] = currentCategories;


    $(".question-box").click(function(){
        var points_id = $(this).children('.points');
        var question_id = $(this).children('.question');

        if((question_id.get(0).id).includes('cat1')){
            var category = categoryOne;
        }else if((question_id.get(0).id).includes('cat2')){
            var category = categoryTwo;
        }else if((question_id.get(0).id).includes('cat3')){
            var category = categoryThree;
        }

        if((question_id.get(0).id).includes('q1')){
            var difficulty = 'easy';
        }else if((question_id.get(0).id).includes('q2')){
            var difficulty = 'medium';
        }else if((question_id.get(0).id).includes('q3')){
            var difficulty = 'hard';
        }

               
        $.ajax({
            url: "https://opentdb.com/api.php?\
                amount=1&\
                category=" + category + "&\
                difficulty=" + difficulty + "&\
                type=multiple",
            success: function(data) {
                var questionTemplate = "<div id='cat1-q3-question' class='question'>\n"
                                        + "<p>{data.question}</p>\n"
                                        + "<div class='form-group ml-3'>\n"
                                            + "<div class='radio'>\n"
                                            + "<label><input type='radio' name='cat1-q3-answer'>Option 1</label>\n"
                                            + "</div>\n"
                                            + "<div class='radio'>\n"
                                                + "<label><input type='radio' name='cat1-q3-answer'>Option 2</label>\n"
                                            + "</div>\n"
                                            + "<div class='radio disabled'>\n"
                                                + "<label><input type='radio' name='cat1-q3-answer'>Option 3</label>\n"
                                            + "</div>\n"
                                        + "</div>\n"
                                    + "</div>"
            }
        })
    })
    
    // var test = "cat1-q3-question";
    // var q2 = "q2";
    // var q3 = "q3";
    
    // if (test.includes(q3)){
    //     console.log('q3 found')
    // }else{
    //     console.log('q3 not found')
    // }
    
    

});
