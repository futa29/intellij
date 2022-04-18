// console.log('fafa');
// let hello =  'aaaa';
// hello = 'konnniti'
// console.log(hello);

// const body = document.querySelector('body');

// divMain.style.marginTop = '5em';

// function showAlert(){
//     alert('ボタンを押しました？')
// }


// document.querySelector('li').addEventListener('click',showAlert);


const answerList = document.querySelectorAll('ol.answers li');

answerList.forEach(li => li.addEventListener('click',checkclickAnswer));

//　正しい答え
const correctAnswers = {
    question1: 'C',

    question2: 'D',

    question3: 'D',

    question4: 'C',

};
function checkclickAnswer(event){
    //クリックされた答えの要素
    const clickAnswerelement = event.currentTarget;
    console.log(clickAnswerelement.dataset.answer);
    //選択した答え（A,B,C,D）
    const selectedAnswer = clickAnswerelement.dataset.answer;

    const questionId = clickAnswerelement.closest('ol.answers').dataset.id;
    console.log(questionId);
    //正しい答え（A,B,C,D）
    const correctAnswer = correctAnswers[questionId];
    console.log(correctAnswer);



    //メッセージを入れる変数を用意
    let message;
    let answerColorCode;



    if(selectedAnswer === correctAnswer){
        //正しい答えだったとき
        message = 'おめでとう！正解です';
        answerColorCode = '';
    }else{
        //間違った答えだったとき
        message = 'ざんねん！不正解です';
        answerColorCode = 'rgb(248, 11, 11)';
    }

    //カラーコードを入れる変数を用意
   
    

    alert(message);

   
    //色を変更　間違ったときだけ
    document.querySelector('span#correct-answer').style.color = answerColorCode;
    //答えを表示
    document.querySelector('div#section-answer').style.display = 'block';
}




