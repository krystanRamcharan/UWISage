<template>
    <form class="registration-container" @submit.prevent="submitForm">
      <div class="registration-form">
        <div class="form-group">
          <label for="uwiEmail" class="form-label">UWI Email</label>
          <input
              type="email"
              id="uwiEmail"
              v-model="form.uwiEmail"
              placeholder="Enter your UWI email"
              class="form-input"
              @blur="validateEmail"
              required
          />
          <span v-if="errors.uwiEmail" class="error-message">{{ errors.uwiEmail }}</span>
        </div>

        <div class="form-group">
          <label for="password" class="form-label">Password</label>
          <input
              type="password"
              id="password"
              v-model="form.password"
              placeholder="Enter your password"
              class="form-input"
              @blur="validatePassword"
              required
          />
          <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
        </div>

        <div class="form-group">
          <label for="confirmPassword" class="form-label">Confirm Password</label>
          <input
              type="password"
              id="confirmPassword"
              v-model="form.confirmPassword"
              placeholder="Confirm your password"
              class="form-input"
              @blur="validateConfirmPassword"
              required
          />
          <span v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</span>
        </div>

        <div class="form-group">
          <label for="username" class="form-label">Username</label>
          <input
              type="text"
              id="username"
              v-model="form.username"
              placeholder="Choose a username"
              class="form-input"
              @blur="validateUsername"
              required
          />
          <span v-if="errors.username" class="error-message">{{ errors.username }}</span>
        </div>

        <button
            type="submit"
            class="submit-button"
            :disabled="isSubmitting"
        >
          {{ isSubmitting ? 'Registering...' : 'Register' }}
        </button>

        <div class="sign-in-prompt">
          <span>Already have an account?</span>
          <router-link to="/sign_in" class="sign-in-link">Sign In</router-link>
        </div>
      </div>
    </form>
  </template>

<style scoped>
.error-message{
  color: red;
  font-family: sans-serif;
  font-size: 14px;
}
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
  background-color: #3350cc;
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
  color: #4467ff;
  text-decoration: none;
  margin-left: 0.5rem;
}

.sign-in-link:hover,
.sign-in-link:focus {
  text-decoration: underline;
}
</style>

<script>
export default {
  data() {
    return {
      form: {
        uwiEmail: '',
        password: '',
        confirmPassword: '',
        username: ''
      },
      errors: {
        uwiEmail: '',
        password: '',
        confirmPassword: '',
        username: ''
      },
      isSubmitting: false
    }
  },
  methods: {
    validateEmail() {
      this.errors.uwiEmail = ''
      if (!this.form.uwiEmail) {
        this.errors.uwiEmail = 'Email is required'
        return false
      }
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailRegex.test(this.form.uwiEmail)) {
        this.errors.uwiEmail = 'Please enter a valid email address'
        return false
      }

      if (!this.form.uwiEmail.toLowerCase().endsWith('@uwi.edu') &&
          !this.form.uwiEmail.toLowerCase().endsWith('@mymona.uwi.edu') &&
          !this.form.uwiEmail.toLowerCase().endsWith('@sta.uwi.edu') &&
          !this.form.uwiEmail.toLowerCase().endsWith('@cavehill.uwi.edu')) {
        this.errors.uwiEmail = 'Please use your UWI email address'
        return false
      }

      return true
    },

    validatePassword() {
      this.errors.password = ''

      if (!this.form.password) {
        this.errors.password = 'Password is required'
        return false
      }

      if (this.form.password.length < 8) {
        this.errors.password = 'Password must be at least 8 characters long'
        return false
      }

      const hasUpperCase = /[A-Z]/.test(this.form.password)
      const hasLowerCase = /[a-z]/.test(this.form.password)
      const hasNumbers = /\d/.test(this.form.password)

      if (!hasUpperCase || !hasLowerCase || !hasNumbers) {
        this.errors.password = 'Password must contain at least one uppercase letter, one lowercase letter, and one number'
        return false
      }

      return true
    },

    validateConfirmPassword() {
      this.errors.confirmPassword = ''

      if (!this.form.confirmPassword) {
        this.errors.confirmPassword = 'Please confirm your password'
        return false
      }

      if (this.form.password !== this.form.confirmPassword) {
        this.errors.confirmPassword = 'Passwords do not match'
        return false
      }

      return true
    },

    validateUsername() {
      this.errors.username = ''

      if (!this.form.username) {
        this.errors.username = 'Username is required'
        return false
      }

      if (this.form.username.length < 3 || this.form.username.length > 20) {
        this.errors.username = 'Username must be between 3 and 20 characters'
        return false
      }

      const usernameRegex = /^[a-zA-Z0-9_]+$/
      if (!usernameRegex.test(this.form.username)) {
        this.errors.username = 'Username can only contain letters, numbers, and underscores'
        return false
      }

      return true
    },

    validateForm() {
      const isEmailValid = this.validateEmail()
      const isPasswordValid = this.validatePassword()
      const isConfirmPasswordValid = this.validateConfirmPassword()
      const isUsernameValid = this.validateUsername()

      return isEmailValid && isPasswordValid && isConfirmPasswordValid && isUsernameValid
    },

    async submitForm() {
      this.isSubmitting = true;

      if (!this.validateForm()) {
        this.isSubmitting = false;
        return;
      }

      try {
        const response = await fetch('http://localhost:5000/api/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            uwiEmail: this.form.uwiEmail,
            password: this.form.password,
            username: this.form.username
          })
        });

        const data = await response.json();

        if (!response.ok) {
          alert(data.error || 'Registration failed');
          return;
        }

        alert(data.message || 'Registration successful');
        console.log('User registered:', data);

        this.form.uwiEmail = '';
        this.form.password = '';
        this.form.confirmPassword = '';
        this.form.username = '';
        this.errors = {};

        this.$router.push('/sign_in');

      } catch (error) {
        console.error('Registration failed:', error);
        alert('An error occurred while registering. Please try again.');
      } finally {
        this.isSubmitting = false;
      }
    }

  }
}

</script>