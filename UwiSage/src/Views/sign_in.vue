<template>
  <div class="login-container">
    <div class="login-wrapper">
      <h1 class="login-title">Login</h1>
      <form class="login-form" @submit.prevent="handleSubmit">
        <div class="form-field">
          <label for="email" class="form-label">UWI Email</label>
          <input id="email" v-model="email" type="email" class="form-input" placeholder="Enter your UWI email" required>
        </div>
        <div class="form-field">
          <label for="password" class="form-label">Password</label>
          <input id="password" v-model="password" type="password" class="form-input" placeholder="Enter your password" required>
        </div>
        <button type="submit" class="submit-button">Sign Up</button>
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
  background-color: #808080;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 6px 80px 50px;
  font: 400 16px Inter, sans-serif;
}

.login-wrapper {
  display: flex;
  width: 700px;
  max-width: 100%;
  flex-direction: column;
  position: relative;
}

.login-title {
  position: absolute;
  top: 60px;
  left: 53%;
  transform: translateX(-50%);
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  color: #333;
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid #000;
}

.login-form {
  border-radius: 8px;
  background-color: #fff;
  display: flex;
  min-width: 320px;
  margin-top: 60px; /* Adjusted to make space for title */
  min-height: 460px;
  width: 100%;
  flex-direction: column;
  justify-content: start;
  padding: 50px 24px; /* Reduced padding so it doesn't push inputs too low */
  border: 1px solid #d9d9d9;
}

.form-field {
  display: flex;
  width: 100%;
  flex-direction: column;
  justify-content: start;
  margin-bottom: 24px;
}

.form-label {
  color: #1e1e1e;
  line-height: 22px;
  margin-bottom: 8px;
}

.form-input {
  border-radius: 8px;
  background-color: #fff;
  width: 95%;
  color: #b3b3b3;
  line-height: 1;
  padding: 12px 16px;
  border: 1px solid #d9d9d9;
}

.submit-button {
  border-radius: 8px;
  background-color: #2c2c2c;
  color: #f5f5f5;
  width: 100%;
  padding: 12px;
  border: 1px solid #2c2c2c;
  cursor: pointer;
}

.register-prompt {
  margin-top: 24px;
  width: 100%;
  color: #1e1e1e;
  text-decoration: underline;
  line-height: 1.4;
}

.register-link {
  color: #0000ff;
  text-decoration: none;
}

@media (max-width: 991px) {
  .login-container {
    padding: 100px 20px;
  }

  .login-title {
    top: 10px;
    font-size: 20px;
  }

  .login-form {
    padding: 40px 20px;
  }
}
</style>
