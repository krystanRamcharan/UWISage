<template>
  <div class="landing-page">
    <header class="header">
      <div class="logo" v-html="logoSvg"></div>
      <nav class="navigation">
        <a href="#features" class="nav-link">Features</a>
        <a href="#register" class="nav-link">Register</a>
        <a href="#login" class="nav-link">Login</a>
      </nav>
      <div class="auth-buttons">
        <router-link to="/sign_in">
          <button class="sign-in-btn">Sign In</button>
        </router-link>
        <router-link to="/sign_up">
          <button class="sign-up-btn">Sign Up</button>
        </router-link>
      </div>
    </header>

    <main>
      <section class="hero">
        <div class="hero-content">
          <div class="welcome-badge">
            <div class="welcome-icon"></div>
            <span class="welcome-text">Welcome to sage</span>
          </div>
          <h1 class="hero-title">SAGE IS AN AI ASSISTANT TO GUIDE UWI STUDENTS</h1>
        </div>
        <div class="hero-cta">
          <p class="hero-description">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
            interdum lacus in erat feugiat feugiat. Phasellus interdum varius
            augue, pellentesque molestie ante.
          </p>
          <button class="cta-button">Get started</button>
        </div>
      </section>

      <section class="how-to-use">
        <div class="how-to-use-content">
          <div class="section-header">
            <h2 class="section-title">HOW TO USE SAGEUWI</h2>
            <p class="section-description">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
              interdum lacus in erat feugiat feugiat. Phasellus interdum varius
              augue, pellentesque molestie ante.
            </p>
          </div>
          <div class="divider"></div>
        </div>
        <div class="chatbot-preview">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/ad33659c33381eac40061641b81f19d65a13ad9f" alt="chatbot" class="chatbot-img" />
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/e77880d937b41949aab7b32129e5e283d8be7ce9" alt="chatbot" class="chatbot-overlay" />
          <div class="chatbot-color-overlay"></div>
        </div>
      </section>

      <section class="cta-section">
        <div class="cta-content">
          <h2 class="cta-title">Maximize your study and learning with SAGEUWI</h2>
          <p class="cta-description">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
            convallis pellentesque mollis. Donec a porttitor dui. Donec at varius
            ex, eget volutpat nunc.
          </p>
          <div class="cta-actions">
            <button class="start-free-btn">Get started for free</button>
            <button class="watch-video-btn" v-html="videoIconSvg"></button>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'SageUwiLanding',
  data() {
    return {
      logoSvg: `<svg id="I2042:2079;13:1083" layer-name="Logo" width="203" height="41" viewBox="0 0 203 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="logo" style="width: 203px; height: 41px">
        <path d="M0 20.44C0 9.25211 9.06956 0.182556 20.2574 0.182556H45.7426C56.9304 0.182556 66 9.25211 66 20.44C66 31.6278 56.9304 40.6974 45.7426 40.6974H20.2574C16.4062 40.6974 12.806 39.6227 9.74029 37.7568C8.59174 37.0578 1.63704 41.6036 0.653465 40.6974C-0.174975 39.9341 4.94158 33.7466 4.24966 32.8558C1.58599 29.4265 0 25.1185 0 20.44Z" fill="url(#paint0_linear_2100_128)"></path>
        <path d="M46.9599 15.0554C47.1048 14.6925 47.6727 14.684 47.8251 15.0438C48.2912 16.1443 49.0681 17.7645 49.9039 18.6003C50.7012 19.3977 52.0843 20.0134 53.0736 20.3812C53.4401 20.5175 53.4676 21.0902 53.1138 21.2566C52.1316 21.7186 50.7359 22.463 49.9039 23.295C49.0248 24.174 48.2436 25.6823 47.7899 26.6674C47.6348 27.0041 47.1172 27.0041 46.9622 26.6674C46.5085 25.6823 45.7272 24.174 44.8482 23.295C44.0075 22.4543 42.5913 21.703 41.6076 21.2422C41.2567 21.0778 41.2795 20.5165 41.6416 20.3785C42.6252 20.0035 44.021 19.3788 44.8482 18.6003C45.7841 17.7195 46.5277 16.1374 46.9599 15.0554Z" fill="white" fill-opacity="0.6"></path>
        <circle cx="29.0002" cy="21.1827" r="4" fill="white" fill-opacity="0.6"></circle>
        <circle cx="16.0002" cy="21.1827" r="4" fill="white" fill-opacity="0.6"></circle>
        <text fill="white" xml:space="preserve" style="white-space: pre" font-family="Abril Fatface" font-size="24" letter-spacing="0.02em"><tspan x="90" y="29.704">SAGE</tspan></text>
        <text fill="url(#paint1_linear_2100_128)" xml:space="preserve" style="white-space: pre" font-family="Abril Fatface" font-size="24" letter-spacing="0.02em"><tspan x="152.67" y="29.704">UWI</tspan></text>
        <defs>
        <linearGradient id="paint0_linear_2100_128" x1="33.3267" y1="40.6974" x2="32.3465" y2="-0.470905" gradientUnits="userSpaceOnUse">
        <stop stop-color="#5599FF"></stop>
        <stop offset="0.836794" stop-color="#7241FF"></stop>
        <stop offset="1" stop-color="#8E66FF"></stop>
        </linearGradient>
        <linearGradient id="paint1_linear_2100_128" x1="165.532" y1="12.6446" x2="203.378" y2="29.4755" gradientUnits="userSpaceOnUse">
        <stop offset="0.0695937" stop-color="#4467FF"></stop>
        <stop offset="1" stop-color="#7241FF"></stop>
        </linearGradient>
        </defs>
        </svg>`,
      videoIconSvg: `<svg id="2042:1672" width="137" height="21" viewBox="0 0 137 21" fill="none" xmlns="http://www.w3.org/2000/svg" class="video-icon" style="width: 137px; height: 21px">
        <path d="M11.7061 7.00337C14.4899 8.54992 15.8817 9.32319 15.8817 10.5C15.8817 11.6768 14.4899 12.4501 11.7061 13.9966L5.94257 17.1986C3.29518 18.6693 1.97149 19.4047 0.985744 18.8247C-7.75645e-07 18.2447 -7.09455e-07 16.7304 -5.77075e-07 13.7019L-2.97153e-07 7.29806C-1.64772e-07 4.26955 -9.85824e-08 2.7553 0.985744 2.17529C1.97149 1.59527 3.29518 2.33066 5.94257 3.80143L11.7061 7.00337Z" fill="white"></path>
        <text fill="white" xml:space="preserve" style="white-space: pre" font-family="ABeeZee" font-size="18" letter-spacing="0em"><tspan x="30" y="16.422">Watch Video</tspan></text>
        </svg>`
    };
  }
};
</script>

<style scoped>
.landing-page {
  min-height: 100vh;
  width: 100%;
  background-color: #010314;
  display: flex;
  flex-direction: column;
}


.header {
  width: 80%;
  padding: 28px 5%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #010314;
}


.navigation {
  display: flex;
  padding: 16px 32px;
  justify-content: center;
  align-items: center;
  gap: 40px;
  border-radius: 40px;
}

.nav-link {
  color: #77798f;
  font: 400 16px ABeeZee;
  text-decoration: none;
}

.auth-buttons {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.sign-in-btn {
  width: 138px;
  padding: 16px 40px;
  border-radius: 40px;
  border: 1px solid #2a2b3a;
  color: #fff;
  font: 16px ABeeZee;
  background-color: transparent;
  cursor: pointer;
}

.sign-up-btn {
  padding: 16px 40px;
  border-radius: 40px;
  border: 1.5px solid #4467ff;
  box-shadow: 0px 0px 10px 0px #74f;
  color: #fff;
  font: 16px ABeeZee;
  background-color: transparent;
  cursor: pointer;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 22px;
  margin-top: 100px;
  padding: 0 20px;
}

.hero-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 22px;
}

.welcome-badge {
  display: flex;
  align-items: center;
  gap: 12px;
}

.welcome-icon {
  width: 27px;
  height: 26px;
  background: linear-gradient(95deg, #4467ff 13.23%, #7241ff 81.63%);
}

.welcome-text {
  letter-spacing: 6.4px;
  text-transform: uppercase;
  background: linear-gradient(95deg, #627fff 8.51%, #865bff 94.21%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font: 400 16px ABeeZee;
}

.hero-title {
  width: 100%;
  max-width: 1064px;
  text-align: center;
  background: radial-gradient(
    70.71% 70.71% at 50% 50%,
    #fff 30%,
    rgba(255, 255, 255, 0.5) 84.77%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font: 700 76px/120% "Abhaya Libre";
}

.hero-cta {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.hero-description {
  width: 677px;
  color: #77798f;
  text-align: center;
  font: 400 24px/160% ABeeZee;
}

.cta-button {
  padding: 22px 40px;
  border-radius: 40px;
  border: 1.5px solid #4467ff;
  box-shadow: 0px 0px 10px 0px rgba(119, 68, 255, 0.7);
  color: #fff;
  background-color: #010314;
  font: 18px ABeeZee;
  cursor: pointer;
}

.how-to-use {
  display: flex;
  width: 80%;
  padding: 100px;
  justify-content: space-between;
  align-items: center;
  border-radius: 30px;
  border-top: 2px solid #4467ff;
  border-bottom: 2px solid #4467ff;
  box-shadow: 0px 16px 80px 0px rgba(102, 77, 255, 0.1);
  margin: 100px auto;
  background-color: #010314;
}

.how-to-use-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 34px;
}

.section-header {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 32px;
}

.section-title {
  background: radial-gradient(
    70.71% 70.71% at 50% 50%,
    #fff 30%,
    rgba(255, 255, 255, 0.5) 84.77%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font: 700 54px/120% "Abhaya Libre";
}

.section-description {
  width: 745px;
  color: #77798f;
  font: 400 26px/160% ABeeZee;
}

.divider {
  width: 743px;
  height: 1px;
  background-color: #182542;
}

.chatbot-preview {
  width: 497px;
  height: 410px;
  position: relative;
}
.chatbot-img {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.chatbot-overlay {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.chatbot-color-overlay {
  width: 100%;
  height: 100%;
  background: linear-gradient(95deg, #4467ff 13.23%, #7241ff 81.63%);
  mix-blend-mode: color;
  position: absolute;
  top: 0;
  left: 0;
}

.cta-section {
  width: 1260px;
  height: 614px;
  margin: 100px auto;
  border-radius: 50px;
  border-top: 2px solid #664dff;
  background: radial-gradient(
    217.23% 100.08% at 50% 18.33%,
    rgba(0, 0, 0, 0) 21.67%,
    #63e 69.34%,
    #fff 100%
  );
}

.cta-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 32px;
  padding: 100px;
}

.cta-title {
  width: 805px;
  text-align: center;
  background: radial-gradient(
    70.71% 70.71% at 50% 50%,
    #fff 30%,
    rgba(255, 255, 255, 0.5) 84.77%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font: 700 54px/120% "Abhaya Libre";
}

.cta-description {
  width: 656px;
  color: #77798f;
  text-align: center;
  font: 400 18px/160% ABeeZee;
}

.cta-actions {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
}

.start-free-btn {
  padding: 22px 40px;
  border-radius: 40px;
  border: 1.5px solid #4467ff;
  box-shadow: 0px 0px 10px 0px rgba(119, 68, 255, 0.7);
  color: #fff;
  background-color: #010314;
  font: 18px ABeeZee;
  cursor: pointer;
}

.watch-video-btn {
  display: flex;
  width: 245px;
  height: 66px;
  padding: 22px 40px;
  justify-content: center;
  align-items: center;
  border-radius: 40px;
  border: 1.5px solid #2a2b3a;
  background-color: #010314;
  cursor: pointer;
}

@media (max-width: 991px) {
  .header {
    padding: 20px;
  }

  .navigation {
    padding: 12px 20px;
    gap: 20px;
  }

  .hero-title {
    font-size: 56px;
  }

  .hero-description {
    width: 100%;
    font-size: 20px;
  }

  .how-to-use {
    width: 90%;
    padding: 50px;
    flex-direction: column;
    gap: 50px;
  }

  .how-to-use-content {
    width: 100%;
  }

  .section-description {
    width: 100%;
  }

  .divider {
    width: 100%;
  }

  .chatbot-preview {
    width: 100%;
    height: auto;
  }

  .cta-section {
    width: 90%;
    height: auto;
  }

  .cta-content {
    padding: 50px;
  }

  .cta-title,
  .cta-description {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .header {
    padding: 16px;
  }

  .navigation {
    display: none;
  }

  .hero-title {
    font-size: 40px;
  }

  .hero-description {
    font-size: 18px;
  }

  .how-to-use {
    padding: 30px;
  }

  .cta-content {
    padding: 30px;
  }

  .cta-actions {
    flex-direction: column;
    width: 100%;
  }

  .start-free-btn,
  .watch-video-btn {
    width: 100%;
  }
}
</style>