<template>
  <div class="sage-assist-container">
    <div class="content-wrapper">
      <div class="content-inner">
        <h1 class="sage-title">SAGE ASSIST</h1>
        <div class="main-content">
          <div class="text-content">
            <h2 class="main-heading">SAGE HELPS UWI STUDENTS WITH STUDY PLANS</h2>
            <div class="cta-wrapper">
              <div class="cta-icon">→</div>
              <button class="cta-button" @click="startAssist" tabindex="0">Let's Start</button>
            </div>
c          </div>
          <div class="image-container">
            <div class="image-wrapper">
              <img src="https://placehold.co/400x400/1B1464/1B1464" alt="Robotic hand" class="robot-image" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SageAssistComponent',
  methods: {
    startAssist() {
      // Implement the start assist functionality here
      console.log('Starting Sage Assist');
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.sage-assist-container {
  display: flex;
  min-height: 100vh;
  width: 100%;
  background-color: #f5fffd;
  font-family: Inter, sans-serif;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 32px 48px;
}

.content-inner {
  display: flex;
  flex-direction: column;
  gap: 48px;
}

.sage-title {
  color: #15c3a7;
  font-size: 64px;
  font-weight: 700;
  letter-spacing: -0.02em;
  width: 100%;
}

.main-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 48px;
}

.text-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 600px;
}

.main-heading {
  color: #111827;
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.cta-wrapper {
  display: flex;
  align-items: center;
}

.cta-icon {
  font-size: 24px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: #15c3a7;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cta-button {
  color: #15c3a7;
  font-size: 24px;
  font-weight: 600;
  margin-left: 16px;
  background: none;
  border: none;
  cursor: pointer;
}

.image-container {
  flex-shrink: 0;
}

.image-wrapper {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background-color: #1b1464;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.robot-image {
  max-width: 100%;
  max-height: 100%;
}

@media (max-width: 991px) {
  .content-wrapper {
    padding: 0 32px;
  }

  .content-inner {
    gap: 32px;
  }

  .sage-title {
    font-size: 48px;
  }

  .main-content {
    flex-direction: column;
    align-items: flex-start;
  }

  .main-heading {
    font-size: 28px;
  }

  .image-wrapper {
    width: 300px;
    height: 300px;
  }
}

@media (max-width: 640px) {
  .content-wrapper {
    padding: 0 16px;
  }

  .content-inner {
    gap: 24px;
  }

  .sage-title {
    font-size: 36px;
  }

  .main-heading {
    font-size: 24px;
  }

  .image-wrapper {
    width: 250px;
    height: 250px;
  }
}
</style>