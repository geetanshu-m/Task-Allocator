import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/client',
    name: 'Client',
    component: () => import('../views/client/index.vue'),
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/admin/index.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
