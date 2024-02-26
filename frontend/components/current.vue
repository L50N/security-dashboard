<template>
  <div class="flex flex-row items-center">
    <div class="flex items-center space-x-3 select-none">
      <div class="text-gray-300 hover:text-gray-400 cursor-pointer transition-all delay-100 ease-in-out">
        <nuxt-link to="/dashboard">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
            <path fill-rule="evenodd"
              d="M9.293 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 17 11h-1v6a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6H3a1 1 0 0 1-.707-1.707l7-7Z"
              clip-rule="evenodd" />
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

    <div @click="toggleMenu" class="inline-block xl:hidden w-full">
      <div class="flex justify-end opacity-40 hover:opacity-70 transition-all delay-100 ease-in-out cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
        </svg>
      </div>
    </div>

    <div v-show="showMenu" class="h-screen w-screen absolute z-40 bg-[#F8F8F8] top-0 left-0">
      <div class="px-9 py-[28px]">
        <div class="px-3 flex flex-row items-center">
          <div>
          <a class="hover:opacity-80 transition-all delay-100 ease-in-out" href="/">
            <img src="/secutiry-dashboard-black.png" class="h-10 w-11">
          </a>
        </div>
        <div @click="toggleMenu"
          class="w-full flex justify-end opacity-40 hover:opacity-70 transition-all delay-100 ease-in-out cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
          </svg>
        </div>
        </div>
        <div class="mt-10 space-y-1">
          <div
          :class="{ 'bg-[#f5f4f4]': $route.path === '/dashboard', 'text-primary rounded-lg': $route.path === '/dashboard' }"
          class="cursor-pointer hover:bg-[#f5f4f4] rounded-lg">
          <nuxt-link to="/dashboard" class="flex flex-row space-x-2 items-center py-2 px-4 rounded-lg">
            <div :class="{ 'text-primary': $route.path === '/dashboard' }" class="text-[15px]">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                :stroke="($route.path === '/dashboard') ? 'currentColor' : 'gray'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Dashboard</p>
          </nuxt-link>
        </div>

        <div
          :class="{ 'bg-[#f5f4f4]': $route.path === '/firewall', 'text-primary rounded-lg': $route.path === '/firewall' }"
          class="cursor-pointer hover:bg-[#f5f4f4] rounded-lg">
          <nuxt-link to="/firewall" class="flex flex-row space-x-2 items-center py-2 px-4 rounded-lg">
            <div :class="{ 'text-primary': $route.path === '/firewall' }" class="text-[15px]">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                :stroke="($route.path === '/firewall') ? 'currentColor' : 'gray'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.047 8.287 8.287 0 0 0 9 9.601a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z" />
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M12 18a3.75 3.75 0 0 0 .495-7.468 5.99 5.99 0 0 0-1.925 3.547 5.975 5.975 0 0 1-2.133-1.001A3.75 3.75 0 0 0 12 18Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Firewall</p>
          </nuxt-link>
        </div>

        <div
          :class="{ 'bg-[#f5f4f4]': $route.path === '/wireguard', 'text-primary rounded-lg': $route.path === '/wireguard' }"
          class="cursor-pointer hover:bg-[#f5f4f4] rounded-lg">
          <nuxt-link to="/wireguard" class="flex flex-row space-x-2 items-center py-2 px-4 rounded-lg">
            <div :class="{ 'text-primary': $route.path === '/wireguard' }" class="text-[15px]">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                :stroke="($route.path === '/wireguard') ? 'currentColor' : 'gray'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M5.25 14.25h13.5m-13.5 0a3 3 0 0 1-3-3m3 3a3 3 0 1 0 0 6h13.5a3 3 0 1 0 0-6m-16.5-3a3 3 0 0 1 3-3h13.5a3 3 0 0 1 3 3m-19.5 0a4.5 4.5 0 0 1 .9-2.7L5.737 5.1a3.375 3.375 0 0 1 2.7-1.35h7.126c1.062 0 2.062.5 2.7 1.35l2.587 3.45a4.5 4.5 0 0 1 .9 2.7m0 0a3 3 0 0 1-3 3m0 3h.008v.008h-.008v-.008Zm0-6h.008v.008h-.008v-.008Zm-3 6h.008v.008h-.008v-.008Zm0-6h.008v.008h-.008v-.008Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Wireguard profiles</p>
          </nuxt-link>
        </div>

        <div
          :class="{ 'bg-[#f5f4f4]': $route.path === '/bruteforce', 'text-primary rounded-lg': $route.path === '/bruteforce' }"
          class="cursor-pointer hover:bg-[#f5f4f4] rounded-lg">
          <nuxt-link to="/bruteforce" class="flex flex-row space-x-2 items-center py-2 px-4 rounded-lg">
            <div :class="{ 'text-primary': $route.path === '/bruteforce' }" class="text-[15px]">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                :stroke="($route.path === '/bruteforce') ? 'currentColor' : 'gray'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Bruteforce</p>
          </nuxt-link>
        </div>
        </div>
      </div>
      <div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMenu: false
    }
  },
  computed: {
    breadcrumbs() {
      const paths = this.$route.path.split('/').filter(Boolean);
      const titles = {
        '/dashboard': 'Dashboard',
        '/firewall': 'Firewall',
        '/wireguard': 'Wireguard',
        '/bruteforce': 'Bruteforce',
      };

      return paths.map((path, index) => {
        const to = `/${paths.slice(0, index + 1).join('/')}`;
        const label = titles[to] || path;
        return { to, label };
      });
    },
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    }
  }
};
</script>
