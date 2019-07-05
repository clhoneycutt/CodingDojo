//




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

    function shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;
      
        // While there remain elements to shuffle...
        while (0 !== currentIndex) {
      
          // Pick a remaining element...
          randomIndex = Math.floor(Math.random() * currentIndex);
          currentIndex -= 1;
      
          // And swap it with the current element.
          temporaryValue = array[currentIndex];
          array[currentIndex] = array[randomIndex];
          array[randomIndex] = temporaryValue;
        }
      
        return array;
      }
    
    // Generate 3 categories and set the category names

    const setCategoryNames = () => {
        var currentCategories = threeCategories();
        
        let [categoryOne, categoryTwo, categoryThree] = currentCategories;
        
        let $categoryOne = document.getElementById('cat1-name');
        let $categoryTwo = document.getElementById('cat2-name');
        let $categoryThree = document.getElementById('cat3-name');
        
        $categoryOne.innerHTML = categories[categoryOne]
        $categoryTwo.innerHTML = categories[categoryTwo]
        $categoryThree.innerHTML = categories[categoryThree]

        return currentCategories;
    }
    

    let currentCategories = setCategoryNames();
    let [categoryOne, categoryTwo, categoryThree] = currentCategories;

        // ====Suggestion from FCC discord====
        //  you can disable the default behaviour from within a event listener, if that is what you are looking for
        //  myButton.addEventListener("click", e => {
        //      e.preventDefault()
        //      do something here
        //  })

    $(".question-box").click(function(){
        var pointsBox = $(this).children('.points');
        var questionBox = $(this).children('.question');
        var question_id = questionBox.get(0).id;

        if((question_id).includes('cat1')){
            var category = categoryOne;
        }else if((question_id).includes('cat2')){
            var category = categoryTwo;
        }else if((question_id).includes('cat3')){
            var category = categoryThree;
        }

        if((question_id).includes('q1')){
            var difficulty = 'easy';
        }else if((question_id).includes('q2')){
            var difficulty = 'medium';
        }else if((question_id).includes('q3')){
            var difficulty = 'hard';
        }

        
               
        $.ajax({
            url: "https://opentdb.com/api.php?\
                amount=1&\
                category=" + category + "&\
                difficulty=" + difficulty + "&\
                type=multiple",
            success: function(data) {
                data = data.results[0];

                window.currentAnswer = data.correct_answer;

                let answerOptions = data.incorrect_answers;
                answerOptions.push(data.correct_answer)                
                shuffle(answerOptions);

                
                var questionTemplate = "<p>{{question}}</p>\n"
                                        + "<div id='{{question_id}}_answers' class='form-group ml-3'>\n"
                                            + "<div class='radio'>\n"
                                            + "<label><input type='radio' name='{{question_id}}'>{{option_1}}</label>\n"
                                            + "</div>\n"
                                            + "<div class='radio'>\n"
                                                + "<label><input type='radio' name='{{question_id}}'>{{option_2}}</label>\n"
                                            + "</div>\n"
                                            + "<div class='radio disabled'>\n"
                                                + "<label><input type='radio' name='{{question_id}}'>{{option_3}}</label>\n"
                                            + "</div>\n"
                                            + "<div class='radio disabled'>\n"
                                                + "<label><input type='radio' name='{{question_id}}'>{{option_4}}</label>\n"
                                            + "</div>\n"
                                        + "</div>"

                mustacheData = {
                    question: data.question,
                    question_id: question_id,
                    option_1: answerOptions[0],
                    option_2: answerOptions[1],
                    option_3: answerOptions[2],
                    option_4: answerOptions[3]
                }

                $('#' + question_id).append( Mustache.render(questionTemplate, mustacheData))
                pointsBox.addClass('hidden');
                questionBox.removeClass('hidden');
                
            }
        })
    })
});
