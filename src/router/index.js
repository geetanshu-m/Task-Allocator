import Vue from 'vue';
import VueRouter from 'vue-router';
import admin from '@/views/admin/index.vue';
import client from '@/views/client/index.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/client',
    name: 'Client',
    // component: () => import('../views/client/index.vue'),
    component: client,
  },
  {
    path: '/admin',
    name: 'Admin',
    // component: () => import('../views/admin/index.vue'),
    component: admin,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
