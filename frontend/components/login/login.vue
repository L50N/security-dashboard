<template>
    <div class="flex items-center min-h-screen">
      <div class="container mx-auto">
        <div class="max-w-md mx-auto my-10">
          <div class="text-center">
            <img class="px-7 lg:px-0 py-3" src="/secutiry-dashboard-high-resolution-logo-transparent-edt.png">
          </div>
          <div class="m-7">
            <form action="">
              <div class="mb-6">
                <label for="email" class="block mb-2 text-sm text-gray-600 dark:text-gray-400 select-none">Email Address</label>
                <input
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
                    href="#!"
                    class="select-none text-sm text-gray-400 focus:outline-none focus:text-primary hover:text-primary dark:hover:text-indigo-300"
                  >
                    Forgot password?
                  </a>
                </div>
                <input
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
          <div>
        <div class="cursor-pointer flex justify-center w-full">
          <a class="text-center text-xs text-gray-400" target="_blank" href="https://github.com/L50N">© Security Dashboard 2023 - 2024</a>
        </div>
      </div>
        </div>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login() {
      axios.post('http://localhost:5000/login', {
        email: this.email,
        password: this.password
      }, { withCredentials: true }) // Send credentials with the request
          .then(response => {
            // Assuming successful login, redirect to dashboard
            this.$router.push('/dashboard');
          })
          .catch(error => {
            console.error('Login failed:', error);
          });
    }
  }
}
</script>