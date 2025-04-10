<template>
  <form class="registration-container">
    <div class="registration-form">
      <div class="form-group">
        <label for="uwiEmail" class="form-label">UWI Email</label>
        <input type="email" id="uwiEmail" placeholder="Enter your UWI email" class="form-input" required />
      </div>
      <div class="form-group">
        <label for="password" class="form-label">Password</label>
        <input type="password" id="password" placeholder="Enter your password" class="form-input" required />
      </div>
      <div class="form-group">
        <label for="confirmPassword" class="form-label">Confirm Password</label>
        <input type="password" id="confirmPassword" placeholder="Confirm your password" class="form-input" required />
      </div>
      <div class="form-group">
        <label for="username" class="form-label">Username</label>
        <input type="text" id="username" placeholder="Choose a username" class="form-input" required />
      </div>
      <button type="submit" class="submit-button">Register</button>
      <div class="sign-in-prompt">
        <span>Already have an account?</span>
        <a href="#" class="sign-in-link">Sign In</a>
      </div>
    </div>
  </form>
</template>

<style scoped>
.registration-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  background-color: #aaa;
  padding: 1rem;
}

.registration-form {
  width: 100%;
  max-width: 729px;
  background-color: #ffffff;
  border-radius: 8px;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
}

.form-label {
  color: #1e1e1e;
  font: 16px/140% Inter, sans-serif;
}

.form-input {
  width: 95%;
  min-width: 240px;
  border-radius: 8px;
  color: #b3b3b3;
  padding: 0.75rem 1rem;
  font: 16px/100% Inter, sans-serif;
  border: 1px solid #e5e7eb;
}

.submit-button {
  width: 100%;
  background-color: #333;
  color: #f5f5f5;
  border-radius: 8px;
  padding: 0.75rem 0;
  font: 16px/100% Inter, sans-serif;
  cursor: pointer;
  border: none;
}

.sign-in-prompt {
  font: 16px/100% Inter, sans-serif;
  text-align: center;
}

.sign-in-link {
  color: #333;
  text-decoration: none;
  margin-left: 0.5rem;
}

.sign-in-link:hover,
.sign-in-link:focus {
  text-decoration: underline;
}
</style>