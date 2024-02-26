<template>
  <div class="min-h-screen flex items-center">
    <div class="max-w-md mx-auto my-10">
      <div class="text-center">
        <img class="px-7 lg:px-0 py-3" src="/secutiry-dashboard-high-resolution-logo-transparent-edt.png">
      </div>
      <div class="m-7">
        <form @submit.prevent="login">
          <div class="mb-6">
            <label for="email" class="block mb-2 text-sm text-gray-600 dark:text-gray-400 select-none">Email Address</label>
            <input
              v-model="email"
              type="email"
              name="email"
              id="email"
              placeholder="Your email address"
              class="select-none bg-[#fcfcfc] w-full px-3 py-2 text-sm placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-primary"
            />
          </div>
          <div class="mb-6">
            <div class="flex justify-between mb-2">
              <label for="password" class="text-sm text-gray-600 dark:text-gray-400 select-none">Password</label>
              <a
                href="https://github.com/L50N/security-dashboard/issues/3" target="_blank"
                class="select-none text-sm text-gray-400 focus:outline-none focus:text-primary hover:text-primary dark:hover:text-indigo-300"
              >
                Forgot password?
              </a>
            </div>
            <input
              v-model="password"
              type="password"
              name="password"
              id="password"
              placeholder="Your Password"
              class="select-none bg-[#fcfcfc] w-full px-3 py-2 text-sm placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-primary"
            />
          </div>
          <div class="mb-6">
            <button
              type="submit"
              class="select-none w-full px-3 py-2 text-white bg-primary hover:bg-[#719af3] transition-all delay-100 ease-in-out rounded-md focus:bg-[#7399eb] focus:outline-none"
            >
              Sign in
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  async created() {
    try {
      const response = await fetch('http://localhost:5000/check-login', {
        method: 'GET',
        credentials: 'include'
      });

      if (response.ok) {
        this.$router.push('/dashboard');
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          }),
          credentials: 'include'
        });
        
        if (response.ok) {
          this.$router.push('/dashboard');
        } else {
          const data = await response.json();
          console.error(data.message);
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  }
}
</script>
