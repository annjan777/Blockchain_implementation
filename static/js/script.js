document.getElementById('transactionForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const sender = document.getElementById('sender').value;
    const recipient = document.getElementById('recipient').value;
    const amount = document.getElementById('amount').value;

    fetch('/transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sender, recipient, amount })
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
      }).catch(error => {
          console.error('Error:', error);
      });
});
