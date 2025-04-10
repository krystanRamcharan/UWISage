import { createRouter, createWebHistory } from "vue-router";
import frame667 from "./views/frame667.vue";
import sign_up from "./views/sign_up.vue";
import sign_in from "./views/sign_in.vue";

const routes = [
  { path: "/", component: frame667 },
  { path: "/sign_up", component: sign_up },
  { path: "/sign_in", component: sign_in },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

