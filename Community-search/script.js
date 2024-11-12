const communities = [
    { name: "Anxiety Support Group", description: "A safe space for those dealing with anxiety.", id: 1 },
    { name: "Depression Recovery", description: "Join us to share experiences and support one another.", id: 2 },
    { name: "Stress Management Community", description: "Learn strategies to manage stress effectively.", id: 3 },
    { name: "Bipolar Support Network", description: "Connect with others facing bipolar challenges.", id: 4 },
    { name: "PTSD Survivors Group", description: "A community for those healing from trauma.", id: 5 },
];

function searchCommunities() {
    const query = document.getElementById("search-box").value.toLowerCase();
    const suggestions = document.getElementById("suggestions");
    suggestions.innerHTML = ""; // Clear previous suggestions
    suggestions.style.display = "none"; // Hide suggestions initially

    if (query) {
        const filteredCommunities = communities.filter(community => community.name.toLowerCase().includes(query));
        if (filteredCommunities.length > 0) {
            suggestions.style.display = "block"; // Show suggestions
            filteredCommunities.forEach(community => {
                const suggestionItem = document.createElement("div");
                suggestionItem.className = "suggestion-item";
                suggestionItem.textContent = community.name;
                suggestionItem.onclick = () => displayCommunity(community);
                suggestions.appendChild(suggestionItem);
            });
        }
    }
}

function displayCommunity(community) {
    const communityList = document.getElementById("community-list");
    communityList.innerHTML = ""; // Clear previous community cards

    const communityCard = document.createElement("div");
    communityCard.className = "community-card";
    communityCard.innerHTML = `
        <h2>${community.name}</h2>
        <p>${community.description}</p>
        <button onclick="joinCommunity(${community.id})">Join Community</button>
    `;
    communityList.appendChild(communityCard);
}

function joinCommunity(communityId) {
    alert(`You have joined the community with ID: ${communityId}`);
    // Here you would typically send a request to your backend to join the community
}