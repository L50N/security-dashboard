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
      <div class="px-12 py-[28px]">
        <div @click="toggleMenu"
          class="w-full flex justify-end opacity-40 hover:opacity-70 transition-all delay-100 ease-in-out cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
          </svg>
        </div>
        <div>
          
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
