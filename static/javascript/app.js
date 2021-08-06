let score = 0

setInterval(async function () {
  let timer = $('#timer')
  let time = parseInt($(timer).text())
  time -= 1
  if (time === 0) {
    res = await axios.post('/endgame', {
      score: score
    })
    result = confirm('Time is up')
    if (result) {
      location.href = 'http://127.0.0.1:5000/board'
    }
    else {
      location.href = 'http://127.0.0.1:5000/'
    }
  }
  $(timer).text(time)
}, 1000)

function renderAnswerCorrectiveness(res, guess) {
  if (res.data === 'ok') {
    score += guess.length
    $('#score').text(score)
    $('#result').text(`${guess} is correct.`)
  } 
  else if (res.data === 'not-on-board') {
    $('#result').text(`${guess} is not on the board.`)
  } 
  else if (res.data === 'not-word') {
    $('#result').text(`${guess} is not an accepted word.`)
  }
}

$('#guess-form').submit(async function (evt) {
  evt.preventDefault()

  let form = evt.currentTarget
  let input = form[0]
  let guess = $(input).val()
  
  await axios.post('/guess', {
    guess: guess
  })
  .then(function (res) {
    console.log(res.data)
    renderAnswerCorrectiveness(res, guess)
  })
  .catch(function (err) {
    console.log(err)
  })

  form.reset()
})