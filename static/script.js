document.addEventListener('DOMContentLoaded', () => {
    const storyLog = document.getElementById('story-log');
    const choicesContainer = document.getElementById('choices-container');
    let isTyping = false;

    // Start the game
    fetch('/start', { method: 'POST' })
        .then(response => response.json())
        .then(data => handleResponse(data))
        .catch(err => console.error('Error starting game:', err));

    function handleResponse(data) {
        // Clear previous content ONLY if it's the intro (restart)
        if (data.text && data.text.includes("DELUSIONS EMBRACE")) {
            storyLog.innerHTML = '';
        }

        // Clear choices container to prepare for new choices
        choicesContainer.innerHTML = '';
        choicesContainer.classList.remove('visible');
        choicesContainer.classList.add('hidden');

        if (data.text && data.text.length > 0) {
            // Add a small break before new text if not intro
            if (storyLog.children.length > 0) {
                 const spacer = document.createElement('div');
                 spacer.style.height = "20px";
                 storyLog.appendChild(spacer);
            }

            typeWriterSequence(data.text, 0, () => {
                showChoices(data.choices);
            });
        } else {
            showChoices(data.choices);
        }
    }

    function typeWriterSequence(lines, index, callback) {
        if (index >= lines.length) {
            callback();
            return;
        }

        const line = lines[index];
        const p = document.createElement('p');
        
        // Check for glitch keyword (simple heuristic based on text content or manual marking)
        // In this implementation, we'll just check if the text contains wide spacing "f e a t u r e s"
        if (line.includes("f e a t u r e s")) {
            p.classList.add('glitch');
            p.setAttribute('data-text', line);
        }

        storyLog.appendChild(p);

        // Simple typing effect
        let charIndex = 0;
        const speed = 30; // ms per char

        function typeChar() {
            if (charIndex < line.length) {
                p.textContent += line.charAt(charIndex);
                charIndex++;
                storyLog.scrollTop = storyLog.scrollHeight; // Auto-scroll to bottom
                setTimeout(typeChar, speed + (Math.random() * 20));
            } else {
                // Line finished
                setTimeout(() => {
                    typeWriterSequence(lines, index + 1, callback);
                }, 500); // Pause between lines
            }
        }

        // Handle empty lines as breaks
        if (line.trim() === "") {
            p.innerHTML = "&nbsp;"; // Maintain height
            setTimeout(() => {
                typeWriterSequence(lines, index + 1, callback);
            }, 300);
        } else {
            typeChar();
        }
    }

    function showChoices(choices) {
        if (!choices || choices.length === 0) return;

        choices.forEach((choiceText, index) => {
            const btn = document.createElement('button');
            btn.classList.add('choice-btn');
            btn.textContent = choiceText;
            btn.onclick = () => makeChoice(index, choiceText);
            choicesContainer.appendChild(btn);
        });

        choicesContainer.classList.remove('hidden');
        // Small delay to fade in
        setTimeout(() => {
            choicesContainer.classList.add('visible');
        }, 100);
    }

    function makeChoice(index, choiceText) {
        // Optimistic UI update? No, wait for server.
        // Disable buttons
        const buttons = choicesContainer.querySelectorAll('button');
        buttons.forEach(b => b.disabled = true);

        // Display the user's choice in the log
        if (choiceText) {
            const choiceP = document.createElement('p');
            choiceP.textContent = `> ${choiceText}`;
            choiceP.style.color = 'var(--highlight-color)';
            choiceP.style.fontStyle = 'italic';
            choiceP.style.marginTop = '10px';
            choiceP.style.marginBottom = '20px';
            storyLog.appendChild(choiceP);
            storyLog.scrollTop = storyLog.scrollHeight;
        }

        fetch('/choice', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ choice_index: index })
        })
        .then(response => response.json())
        .then(data => handleResponse(data))
        .catch(err => console.error('Error making choice:', err));
    }
});
