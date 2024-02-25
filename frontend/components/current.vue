<template>
    <div class="flex items-center space-x-3 select-none">
      <div class="text-gray-300 hover:text-gray-400 cursor-pointer transition-all delay-100 ease-in-out">
        <nuxt-link to="/dashboard">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            class="w-5 h-5"
          >
            <path
              fill-rule="evenodd"
              d="M9.293 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 17 11h-1v6a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6H3a1 1 0 0 1-.707-1.707l7-7Z"
              clip-rule="evenodd"
            />
          </svg>
        </nuxt-link>
      </div>

      <div class="text-gray-500">
        <p>/</p>
      </div>
  
      <div class="text-gray-400 flex flex-row space-x-3 text-sm items-center">
        <div v-for="(crumb, index) in breadcrumbs" :key="index">
          <div v-if="index !== 0" class="text-gray-300 text-base">
            <p>/</p>
          </div>
          <div>
            <nuxt-link :to="crumb.to" class="hover:text-gray-500 delay-100 transition-all">
              {{ crumb.label }}
            </nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      breadcrumbs() {
        const paths = this.$route.path.split('/').filter(Boolean);
        const titles = {
          '/dashboard': 'Dashboard',
          '/firewall': 'Firewall',
          '/wg': 'Wireguard',
          '/bruteforce': 'Bruteforce',
        };
  
        return paths.map((path, index) => {
          const to = `/${paths.slice(0, index + 1).join('/')}`;
          const label = titles[to] || path;
          return { to, label };
        });
      },
    },
  };
  </script>
  