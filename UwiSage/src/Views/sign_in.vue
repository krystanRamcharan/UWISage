<template>
  <div class="login-container">
    <div class="login-wrapper">
      <!-- <h1 class="login-title">Login</h1> -->
      <form class="login-form" @submit.prevent="handleSubmit">
        <div class="form-field">
          <label for="email" class="form-label">UWI Email</label>
          <input id="email" v-model="email" type="email" class="form-input" placeholder="Enter your UWI email" required>
        </div>
        <div class="form-field">
          <label for="password" class="form-label">Password</label>
          <input id="password" v-model="password" type="password" class="form-input" placeholder="Enter your password" required>
        </div>
        <button type="submit" class="submit-button">Login</button>
        <p class="register-prompt">
          Don't have an account?
          <a href="/sign_up" class="register-link">Register</a>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await fetch('http://localhost:5000/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            uwiEmail: this.email,
            password: this.password
          })
        });

        const data = await response.json();
        if (!data.token) {
          alert('Invalid response from server.');
          return;
        }

        if (!response.ok) {
          alert(data.error || 'Login failed');
          return;
        }

        localStorage.setItem('jwt_token', data.token);
        localStorage.setItem('username', data.username);

        this.$router.push('/chat');

      } catch (error) {
        console.error('Login error:', error);
        alert('An unexpected error occurred. Please try again.');
      }
    }
  }
}
</script>


<style scoped>
.login-container {
  background-color: #aaa;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 160px 20px;
  min-height: 70vh;
  font-family: 'Inter', sans-serif;
}

.login-wrapper {
  width: 100%;
  max-width: 420px;
  background-color: #fff;
  border-radius: 16px;
  padding: 40px 30px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.login-title {
  font-size: 28px;
  font-weight: 600;
  color: #1e1e1e;
  text-align: center;
  margin-bottom: 30px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-field {
  display: flex;
  flex-direction: column;
}

.form-label {
  color: #333;
  font-weight: 500;
  margin-bottom: 6px;
}

.form-input {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 12px;
  font-size: 15px;
  color: #333;
}

.submit-button {
  background-color: #4467ff;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 12px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.submit-button:hover {
  background-color: #3350cc;
}

.register-prompt {
  margin-top: 20px;
  font-size: 14px;
  text-align: center;
  color: #444;
}

.register-link {
  color: #4467ff;
  text-decoration: none;
  font-weight: 500;
}

.register-link:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .login-wrapper {
    padding: 30px 20px;
  }

  .login-title {
    font-size: 24px;
  }
}
</style>

