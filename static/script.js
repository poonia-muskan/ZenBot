document.addEventListener("DOMContentLoaded", () => {
  const isDashboard = document.querySelector(".chat-input-area") !== null;
  const form = document.querySelector("form.chat-input-area");
  const input = document.getElementById("messageInput");
  const responseBox = document.querySelector(".chat-body");
  const toggleBtn = document.getElementById("sidebarToggleBtn");
  const sidebar = document.getElementById("sidebar");
  const passwordToggles = document.querySelectorAll(".toggle-password");

  toggleBtn?.addEventListener("click", () => {
    sidebar?.classList.toggle("active");
  });
if (isDashboard) {
  input?.focus();

  form?.addEventListener("submit", async function (e) {
    e.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    let convoIdInput = document.querySelector('input[name="conversation_id"]');
    let convoId = convoIdInput ? convoIdInput.value : "";

    const userBubble = document.createElement("div");
    userBubble.classList.add("chat-bubble", "user");
    userBubble.textContent = message;
    responseBox.appendChild(userBubble);
    responseBox.scrollTop = responseBox.scrollHeight;

    input.value = "";
    setTimeout(() => input.focus(), 0);

    const botTyping = document.createElement("div");
    botTyping.classList.add("chat-bubble", "bot");
    botTyping.innerHTML = `<span class="typing">Typing<span class="dots"><span>.</span><span>.</span><span>.</span></span></span>`;
    responseBox.appendChild(botTyping);
    responseBox.scrollTop = responseBox.scrollHeight;

    await new Promise(resolve => setTimeout(resolve, 850));

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Requested-With": "XMLHttpRequest"
        },
        body: JSON.stringify({
          mood: message,
          conversation_id: convoId
        })
      });

      const data = await res.json();
      botTyping.remove();

      const botReply = document.createElement("div");
      botReply.classList.add("chat-bubble", "bot");
      botReply.textContent = data.reply;
      responseBox.appendChild(botReply);
      responseBox.scrollTop = responseBox.scrollHeight;

      if (!convoId && data.conversation_id) {
        if (!convoIdInput) {
          convoIdInput = document.createElement("input");
          convoIdInput.type = "hidden";
          convoIdInput.name = "conversation_id";
          form.appendChild(convoIdInput);
        }
        convoIdInput.value = data.conversation_id;
      }
    } catch (err) {
      botTyping.remove();

      const errorReply = document.createElement("div");
      errorReply.classList.add("chat-bubble", "bot");
      errorReply.textContent = "ZenBot is broken 😭 Please try again later.";
      responseBox.appendChild(errorReply);
      responseBox.scrollTop = responseBox.scrollHeight;
    }
  });

  if (responseBox) {
    responseBox.scrollTop = responseBox.scrollHeight;
  }
}
  const messages = document.querySelectorAll(".message");
  if (messages.length > 0) {
    messages.forEach(msg => {
      setTimeout(() => {
        msg.style.opacity = "0";
        msg.style.transition = "opacity 0.6s ease";
        setTimeout(() => msg.remove(), 800);
      }, 4000);
    });
  }

  passwordToggles.forEach(toggle => {
    toggle.addEventListener("click", () => {
      const input = toggle.previousElementSibling;
      if (input.type === "password") {
        input.type = "text";
        toggle.textContent = "🙈";
      } else {
        input.type = "password";
        toggle.textContent = "👁️";
      }
    });
  });

  const moodBtn = document.getElementById("moodGraphBtn");
  const moodModal = document.getElementById("moodModal");
  const closeBtn = document.querySelector(".modal .close");

  moodBtn?.addEventListener("click", () => {
    moodModal.style.display = "block";

    const canvas = document.getElementById("moodChart");
    if (canvas.chart) {
      canvas.chart.destroy();
    }

    fetch("/mood_data")
      .then(res => res.json())
      .then(data => {
        const labels = [];
        const scores = [];
        const messages = [];

        Object.keys(data).forEach(date => {
          const moods = data[date];
          moods.forEach(entry => {
            labels.push(new Date(date).toLocaleDateString("en-US", {
              month: "short", day: "numeric"
            }));
            scores.push(entry.score);
            messages.push(entry.message);  
          });
        });

        const ctx = document.getElementById("moodChart").getContext("2d");

        new Chart(ctx, {
          type: "line",
          data: {
            labels,
            datasets: [{
              label: "Mood Score",
              data: scores,
              borderColor: "#38bdf8",
              backgroundColor: "rgba(56, 189, 248, 0.2)",
              borderWidth: 2,
              tension: 0.3,
              fill: true,
              pointRadius: 5,
              pointHoverRadius: 7
            }]
          },
          options: {
            responsive: true,
            plugins: {
              title: {
                display: true,
                text: "Your Mood Over Time",
                padding: { top: 10, bottom: 20 },
                font: { size: 18 }
              },
              tooltip: {
                callbacks: {
                  label: function (context) {
                    const idx = context.dataIndex;
                    const score = context.raw;
                    const message = messages[idx];
                    return `Score: ${score} - "${message}"`;
                  }
                }
              },
              legend: {
                labels: {
                  color: "#fff",
                  font: { size: 14 }
                }
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                max: 5,
                ticks: {
                  stepSize: 1,
                  callback: function (value) {
                    const emojiMap = {
                      1: "😢",
                      2: "😞",
                      3: "😐",
                      4: "🙂",
                      5: "😄"
                    };
                    return `${value} ${emojiMap[value] || ""}`;
                  },
                  color: "#fff"
                },
                title: {
                  display: true,
                  text: "Mood Score",
                  color: "#fff"
                }
              },
              x: {
                ticks: {
                  color: "#fff"
                }
              }
            }
          }
        });

        const graphContainer = document.querySelector(".modal-content");
        const legendInfo = document.createElement("p");
        legendInfo.innerHTML = `
          <br><strong>Mood Score Guide:</strong> <br>
          😢 1 - Feeling Low &nbsp; | &nbsp;
          😞 2 - Down &nbsp; | &nbsp;
          😐 3 - Meh &nbsp; | &nbsp;
          🙂 4 - Okay &nbsp; | &nbsp;
          😄 5 - Happy
        `;
        legendInfo.style.color = "#fff";
        legendInfo.style.fontSize = "0.9rem";
        legendInfo.style.textAlign = "center";
        graphContainer.appendChild(legendInfo);
      });
  });

  closeBtn?.addEventListener("click", () => {
    const modal = document.querySelector(".modal");
    modal.style.display = "none";
  });
}); 