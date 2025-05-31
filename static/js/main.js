
function escapeHTML(str) {
  return str.replace(/[&<>"']/g, function(m) {
    return ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
        })[m];
      });
}

function askBot() {
  const question = document.getElementById('userInput').value.trim();
  if (!question) return;
  const botResponse = document.getElementById('botResponse');

  // Add user's question
  const userDiv = document.createElement('div');
  userDiv.className = 'user-message';
  userDiv.innerHTML = '<b>You:</b> ' + escapeHTML(question);
  botResponse.appendChild(userDiv);

  // Show thinking...
  const thinkingDiv = document.createElement('div');
  thinkingDiv.className = 'bot-message';
  thinkingDiv.innerHTML = '<i>Thinking...</i>';
  botResponse.appendChild(thinkingDiv);

  fetch('/api/ask?question=' + encodeURIComponent(question))
    .then(response => response.json())
    .then(data => {
      thinkingDiv.innerHTML = '<b>Bot:</b> ' + escapeHTML(data.answer);
    })
    .catch(error => {
      thinkingDiv.innerHTML = 'Error: ' + error;
    });

  document.getElementById('userInput').value = '';
  botResponse.scrollTop = botResponse.scrollHeight; // Scroll to bottom
}
    // Add event listener for the Ask button and Enter key
    document.getElementById('askBtn').addEventListener('click', askBot);
    document.getElementById('userInput').addEventListener('keydown', function(e) {
      if (e.key === 'Enter') askBot();
    });
  

// api endpoints

function predictXcal() {
    const xValue = [
      parseInt(document.getElementById('x').value, 10)
    ]
    fetch('/api/xcal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ x: xValue })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('requestsList').innerText = 'Error: ' + error;
    });
}
function predictXlng() {
    const xValue = [
      parseInt(document.getElementById('x1').value,10),
      parseInt(document.getElementById('x2').value,10),
      parseInt(document.getElementById('x3').value,10),
      parseInt(document.getElementById('x4').value,10),
      parseInt(document.getElementById('x5').value,10)
      
    ];
    fetch('/api/xlng', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ x: xValue })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('requestsList').innerText = 'Error: ' + error;
    });
}
function predictXdiab() {
    const xValue = [
      
      parseInt(document.getElementById('x1').value,10),
      parseInt(document.getElementById('x2').value,10),
      parseInt(document.getElementById('x3').value,10),
      parseInt(document.getElementById('x4').value,10),
      parseInt(document.getElementById('x5').value,10),
      parseInt(document.getElementById('x6').value,10),
      parseInt(document.getElementById('x7').value,10)

    ];
    fetch('/api/xdiab', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ x: xValue })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('requestsList').innerText = 'Error: ' + error;
    });
}
function requestmarket() {
    const email = document.getElementById('requestm_email').value;
    const text = document.getElementById('requestm_text').value;
    fetch('/api/request_market', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, request: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('requestsListM').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('requestsListM').innerText = 'Error: ' + error;
    });
}

function request() {
    const email = document.getElementById('requestg_email').value;
    const text = document.getElementById('requestg_text').value;
    fetch('/api/Grequest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, request: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('requestsListg').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('requestsListg').innerText = 'Error: ' + error;
    });
}
