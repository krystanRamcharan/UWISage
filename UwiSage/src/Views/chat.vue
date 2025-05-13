<template>
  <div class="chat-container">
    <!-- Left sidebar -->
    <div class="sidebar">
      <div class="sidebar-header">
        <button class="menu-button">
          <span class="menu-icon"></span>
          <span class="menu-icon"></span>
          <span class="menu-icon"></span>
        </button>
      </div>

      <div class="sidebar-content">
        <button class="sidebar-option primary-option">
          <span class="dot-icon primary-dot"></span>
          <span>New Chat</span>
        </button>

        <button class="sidebar-option">
          <span class="dot-icon"></span>
          <span>Recent Chats</span>
        </button>

        <button class="sidebar-option">
          <span>Create Study Schedule</span>
        </button>

        <button class="sidebar-option">
          <span>Recommend Course</span>
        </button>

        <button class="sidebar-option">
          <span>Explain Homework</span>
        </button>
      </div>

      <div class="user-profile">
        <div class="avatar">
          <span>M</span>
        </div>
        <div class="user-info">
          <div class="user-label">Connected as</div>
          <div class="user-name">Michael</div>
        </div>
        <button class="expand-button">
          <span class="chevron-icon">▲</span>
        </button>
      </div>
    </div>
      <!-- Main chat area -->
      <div class="main-content">
        <div class="header">
          <div class="header-actions">
            <button class="alert-button">
              <span class="alert-icon">▲</span>
            </button>
            <button class="trash-button">
              <span class="trash-icon">🗑</span>
            </button>
            <div class="search-container">
              <input type="text"
                     placeholder="Search UWIlinC"
                     class="search-input"
                     v-model="searchQuery"
                     @keyup.enter="performDocSearch" />
              <span class="search-icon" @click="performDocSearch">🔍</span>
            </div>
          </div>
        </div>

        <div class="messages-container" ref="messagesContainer">
          <div v-for="(message, index) in messages" :key="index"
               :class="['message', message.sender === 'user' ? 'user-message' : 'bot-message']">
            <div class="message-content" v-if="!message.isSearchResults && !message.isSchedule">
              {{ message.text }}
            </div>

<!--            &lt;!&ndash; Display search results &ndash;&gt;-->
<!--            <div class="search-results" v-if="message.isSearchResults">-->
<!--              <div class="results-header">-->
<!--                <h3>Search Results for: "{{ message.query }}"</h3>-->
<!--                <p>Found {{ message.results.count }} results</p>-->
<!--              </div>-->
<!--              <div class="result-item" v-for="(result, idx) in message.results.results" :key="idx">-->
<!--                <div class="result-title">-->
<!--                  <a :href="result.link" target="_blank">{{ result.title }}</a>-->
<!--                </div>-->
<!--                <div class="result-snippet">{{ result.snippet }}</div>-->
<!--                <div class="result-meta">Score: {{ result.score }}</div>-->
<!--              </div>-->
<!--            </div>-->
            <!-- Display search results -->
            <div class="search-results" v-if="message.isSearchResults">
              <div class="results-header">
                <h3>Search Results for: "{{ message.query }}"</h3>
                <p>Found {{ message.results.results.length }} results</p>
              </div>

              <table class="search-results-table">
                <thead>
                <tr>
                  <th>#</th>
                  <th>Document</th>
                  <th>Score</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(result, idx) in message.results.results" :key="idx" class="result-row">
                  <td class="result-index">{{ idx + 1 }}</td>
                  <td class="result-content">
                    <a :href="extractLink(result.content)" target="_blank">
                      {{ formatDocumentTitle(result.content, result.doc_id) }}
                    </a>
                    <div class="result-snippet">{{ extractSnippet(result.content) }}</div>
                  </td>
                  <td class="result-score">{{ result.score }}</td>
                </tr>
                </tbody>
              </table>
            </div>
            <!-- Display schedule -->
<!--            <div class="schedule-results" v-if="message.isSchedule">-->
<!--              <div class="schedule-header">-->
<!--                <h3>Your Study Schedule</h3>-->
<!--              </div>-->
<!--              <div class="schedule-item" v-for="(course, timeSlot) in message.schedule" :key="timeSlot">-->
<!--                <div class="schedule-day-time">-->
<!--                  {{ formatTimeSlot(timeSlot) }}-->
<!--                </div>-->
<!--                <div class="schedule-course">{{ course }}</div>-->
<!--              </div>-->
<!--            </div>-->
            <!-- Display schedule as a table -->
            <div class="schedule-results" v-if="message.isSchedule">
              <div class="schedule-header">
                <h3>Your Study Schedule</h3>
              </div>

              <table class="schedule-table">
                <thead>
                <tr>
                  <th>Day</th>
                  <th>Time</th>
                  <th>Course</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(course, timeSlot) in message.schedule" :key="timeSlot" class="schedule-row">
                  <td class="schedule-day">{{ timeSlot.split('_')[0] }}</td>
                  <td class="schedule-time">{{ timeSlot.split('_')[1] }}</td>
                  <td class="schedule-course">{{ course }}</td>
                </tr>
                </tbody>
              </table>
          </div>
            </div>
        </div>

        <div class="input-container">
          <input
              type="text"
              v-model="newMessage"
              @keyup.enter="sendMessage"
              placeholder="Type a new message here"
              class="message-input"
          />
          <div class="input-actions">
            <button class="action-button">
              <span class="attach-icon">📎</span>
            </button>
            <button class="action-button">
              <span class="emoji-icon">😊</span>
            </button>
            <button class="send-button" @click="sendMessage">
              <span class="send-icon">▶</span>
            </button>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'ChatInterface',
  data() {
    return {
      newMessage: '',
      searchQuery: '',
      messages: [],
      isLoading: false
    };
  },
  methods: {
    formatTimeSlot(timeSlot) {
      // Split the timeSlot string (e.g., "Mon_12pm") into day and time
      const [day, time] = timeSlot.split('_');
      return `${day} at ${time}`;
    },
    extractLink(content) {
      // Extract URL from content
      const urlMatch = content.match(/(https?:\/\/[^\s]+)/);
      return urlMatch ? urlMatch[0] : '#';
    },

    formatDocumentTitle(content, docId) {
      // Extract filename from URL
      const urlMatch = content.match(/\/([^\/]+\.pdf)/);
      if (urlMatch) {
        return urlMatch[1];
      }
      // Fallback to doc_id
      return `Document ${docId}`;
    },

    extractSnippet(content) {
      // Get content after the URL
      const parts = content.split('...');
      return parts.length > 1 ? parts[1] : '';
    },

    sendMessage() {
      if (this.newMessage.trim() === '') return;

      // Add user message
      this.messages.push({
        text: this.newMessage,
        sender: 'user'
      });

      const userMessage = this.newMessage;
      this.newMessage = '';

      // Process the message to determine intent
      this.processUserMessage(userMessage);

      // Scroll to bottom after new message
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },

    async processUserMessage(message) {
      this.isLoading = true;

      // Check if it's a search query
      if (message.toLowerCase().includes('search for') || message.toLowerCase().includes('find documents')) {
        // Extract the search query from the message
        let query = message;
        if (message.toLowerCase().includes('search for')) {
          query = message.substring(message.toLowerCase().indexOf('search for') + 11).trim();
        } else if (message.toLowerCase().includes('find documents')) {
          query = message.substring(message.toLowerCase().indexOf('find documents') + 14).trim();
        }

        // Perform the search
        await this.docSearch(query);
      }
      // Check if it's a schedule request
      else if (message.toLowerCase().includes('schedule') ||
          message.toLowerCase().includes('study plan') ||
          message.toLowerCase().includes('create schedule')) {
        // For scheduling, we need busy times and constraints
        // Let's ask the user for these inputs
        this.messages.push({
          text: "I can help create a study schedule. Please share your busy times in the format:\n\nMonday: 9:00-12:00, 15:00-17:00\nTuesday: 10:00-13:00\n...",
          sender: 'bot'
        });

        // Store a flag to indicate that next message should be busy times
        this.expectingBusyTimes = true;
        this.isLoading = false;
      }
      // Check if we're expecting busy times
      else if (this.expectingBusyTimes) {
        // Store busy times and ask for constraints
        this.busyText = message;
        this.expectingBusyTimes = false;
        this.expectingConstraints = true;

        this.messages.push({
          text: "Great! Now, please share any study constraints or preferences (e.g., 'I prefer to study Math in the morning', 'No Biology after 18:00').",
          sender: 'bot'
        });
        this.isLoading = false;
      }
      // Check if we're expecting constraints
      else if (this.expectingConstraints) {
        // Store constraints and generate schedule
        this.constraintsText = message;
        this.expectingConstraints = false;

        // Now we have both busy times and constraints, generate the schedule
        await this.generateSchedule(this.busyText, this.constraintsText);
      }
      // Default response for other types of messages
      else {
        this.messages.push({
          text: `I can help with document searches or creating study schedules. Try saying "Search for [topic]" or "Create a study schedule".`,
          sender: 'bot'
        });
        this.isLoading = false;
      }

      // Scroll to bottom after processing
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },

    async performDocSearch() {
      if (this.searchQuery.trim() !== '') {
        // Add the search query as a user message
        this.messages.push({
          text: `Search for: ${this.searchQuery}`,
          sender: 'user'
        });

        // Perform the search
        await this.docSearch(this.searchQuery);

        // Clear the search input
        this.searchQuery = '';
      }
    },

    async docSearch(query) {
      try {
        // Show loading message
        const loadingMsgIndex = this.messages.length;
        this.messages.push({
          text: `Searching for "${query}"...`,
          sender: 'bot'
        });

        // Make API request to the doc_search endpoint
        const response = await axios.post('http://127.0.0.1:5000/api/search', {
          query: query,
          max_results: 10
        });

        // Remove loading message
        this.messages.splice(loadingMsgIndex, 1);

        // Add search results to messages
        this.messages.push({
          isSearchResults: true,
          query: query,
          results: response.data,
          sender: 'bot'
        });
      } catch (error) {
        console.error('Error during document search:', error);
        this.messages.push({
          text: `An error occurred while searching: ${error.message}`,
          sender: 'bot'
        });
      } finally {
        this.isLoading = false;
      }
    },

    async generateSchedule(busyText, constraintsText) {
      try {
        // Show loading message
        const loadingMsgIndex = this.messages.length;
        this.messages.push({
          text: 'Generating your study schedule...',
          sender: 'bot'
        });

        // Make API request to the schedule endpoint
        const response = await axios.post('http://127.0.0.1:5000/api/schedule', {
          busyText: busyText,
          constraintsText: constraintsText
        });

        // Remove loading message
        this.messages.splice(loadingMsgIndex, 1);

        // Add schedule results to messages
        this.messages.push({
          isSchedule: true,
          schedule: response.data.schedule,
          sender: 'bot'
        });
        console.log(this.messages)
        // Add a follow-up message
        this.messages.push({
          text: 'Here\'s your study schedule based on your availability and preferences. Let me know if you\'d like to make any adjustments!',
          sender: 'bot'
        });
      } catch (error) {
        console.error('Error generating schedule:', error);
        this.messages.push({
          text: `An error occurred while creating your schedule: ${error.message}`,
          sender: 'bot'
        });
      } finally {
        this.isLoading = false;
      }
    },

    scrollToBottom() {
      const container = this.$refs.messagesContainer;
      container.scrollTop = container.scrollHeight;
    }
  },
  mounted() {
    // Initialize with a welcome message
    this.messages.push({
      text: 'Hello! I can help you search for documents or create a study schedule. Try typing "Search for [topic]" or "Create a study schedule".',
      sender: 'bot'
    });
  }
};
</script>
<!--<script>-->
<!--export default {-->
<!--  name: 'ChatInterface',-->
<!--  data() {-->
<!--    return {-->
<!--      newMessage: '',-->
<!--      messages: [-->
<!--        // Sample messages for demonstration-->
<!--        // { text: 'Hello! How can I help you today?', sender: 'bot' },-->
<!--        // { text: 'I need help with my homework', sender: 'user' },-->
<!--      ]-->
<!--    };-->
<!--  },-->
<!--  methods: {-->
<!--    sendMessage() {-->
<!--      if (this.newMessage.trim() === '') return;-->

<!--      // Add user message-->
<!--      this.messages.push({-->
<!--        text: this.newMessage,-->
<!--        sender: 'user'-->
<!--      });-->

<!--      const userMessage = this.newMessage;-->
<!--      this.newMessage = '';-->

<!--      // Simulate bot response (in a real app, this would be an API call)-->
<!--      setTimeout(() => {-->
<!--        this.receiveBotMessage(userMessage);-->
<!--      }, 500);-->
<!--    },-->
<!--    receiveBotMessage(userMessage) {-->
<!--      // In a real implementation, this would be replaced with an actual API call-->
<!--      let botResponse = 'I received your message: "' + userMessage + '". How can I assist you further?';-->

<!--      this.messages.push({-->
<!--        text: botResponse,-->
<!--        sender: 'bot'-->
<!--      });-->

<!--      // Scroll to bottom after new message-->
<!--      this.$nextTick(() => {-->
<!--        this.scrollToBottom();-->
<!--      });-->
<!--    },-->
<!--    scrollToBottom() {-->
<!--      const container = this.$refs.messagesContainer;-->
<!--      container.scrollTop = container.scrollHeight;-->
<!--    }-->
<!--  },-->
<!--  mounted() {-->
<!--    // Initialize with a welcome message-->
<!--    this.messages.push({-->
<!--      text: 'Hello! How can I help you today?',-->
<!--      sender: 'bot'-->
<!--    });-->
<!--  }-->
<!--};-->
<!--</script>-->

<style scoped>
.search-results-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.search-results-table th, .search-results-table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.search-results-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.result-row:hover {
  background-color: #f5f5f5;
}

.result-snippet {
  font-size: 0.9em;
  color: #666;
  margin-top: 4px;
}

.result-index {
  width: 40px;
  text-align: center;
}

.result-score {
  width: 80px;
  text-align: center;
}

.schedule-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.schedule-table th, .schedule-table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.schedule-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.schedule-row:hover {
  background-color: #f5f5f5;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
}

.chat-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  background-color: #f9f9fb;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  overflow: hidden;
}

/* Sidebar styles */
.sidebar {
  display: flex;
  flex-direction: column;
  width: 240px;
  min-width: 240px;
  background-color: #0e0e15;
  color: #ffffff;
  position: relative;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.sidebar-header {
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.menu-button {
  background: none;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  cursor: pointer;
  padding: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
}

.menu-icon {
  width: 14px;
  height: 1px;
  background-color: #ffffff;
  margin: 2px 0;
}

.sidebar-content {
  flex: 1;
  padding: 8px 12px;
  display: flex;
  flex-direction: column;
  gap: 1px;
  margin-top: 8px;
}

.sidebar-option {
  padding: 8px 12px;
  border-radius: 4px;
  background: none;
  border: none;
  color: #6b6b80;
  text-align: left;
  cursor: pointer;
  transition: background-color 0.2s;
  font-size: 13px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.dot-icon {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background-color: #6b6b80;
  display: inline-block;
}

.primary-dot {
  background-color: #ffffff;
}

.sidebar-option:hover {
  background-color: rgba(255, 255, 255, 0.05);
  color: #ffffff;
}

.primary-option {
  background-color: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  font-weight: 500;
}

.user-profile {
  display: flex;
  align-items: center;
  padding: 10px 12px;
  background-color: #15151f;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
  margin-top: auto;
}

.avatar {
  width: 26px;
  height: 26px;
  border-radius: 4px;
  overflow: hidden;
  margin-right: 8px;
  background-color: #ff5733;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: white;
  font-size: 12px;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info {
  flex: 1;
}

.user-label {
  font-size: 9px;
  color: #6b6b80;
}

.user-name {
  font-size: 12px;
  font-weight: 500;
}

.expand-button {
  background: none;
  border: none;
  color: #6b6b80;
  cursor: pointer;
  font-size: 10px;
  padding: 2px;
}

/* Main content styles */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: white;
}

.header {
  padding: 10px 15px;
  border-bottom: 1px solid #eaeaef;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.alert-button, .trash-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 3px;
  font-size: 14px;
}

.alert-icon {
  color: #ff6b6b;
  font-size: 14px;
}

.trash-icon {
  color: #6b6b80;
  font-size: 14px;
}

.search-container {
  flex: 1;
  position: relative;
  max-width: 200px;
  margin-left: auto;
}

.search-input {
  width: 100%;
  padding: 6px 28px 6px 10px;
  border-radius: 4px;
  border: 1px solid #eaeaef;
  background-color: #f5f5f7;
  font-size: 12px;
  color: #333;
}

.search-icon {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  color: #6b6b80;
  font-size: 12px;
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  background-color: #f9f9fb;
}

.message {
  max-width: 70%;
  padding: 10px 14px;
  border-radius: 10px;
  word-break: break-word;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  font-size: 13px;
}

.user-message {
  align-self: flex-end;
  background-color: #2970ff;
  color: white;
}

.bot-message {
  align-self: flex-start;
  background-color: white;
  color: #333;
  border: 1px solid #eaeaef;
}

.input-container {
  display: flex;
  align-items: center;
  padding: 12px 15px;
  background-color: white;
  border-top: 1px solid #eaeaef;
}

.message-input {
  flex: 1;
  padding: 10px 14px;
  border-radius: 6px;
  border: 1px solid #dadae1;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.message-input:focus {
  border-color: #2970ff;
}

.input-actions {
  display: flex;
  align-items: center;
  margin-left: 8px;
}

.action-button {
  background: none;
  border: none;
  cursor: pointer;
  margin: 0 3px;
  color: #6b6b80;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.send-button {
  background-color: #2970ff;
  color: white;
  border: none;
  border-radius: 4px;
  width: 26px;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 10px;
  margin-left: 3px;
}
</style>