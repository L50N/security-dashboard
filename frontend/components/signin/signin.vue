<template>
    <div class="flex items-center min-h-screen bg-white">
        <div class="container mx-auto">
            <div class="max-w-md mx-auto my-10">
                <div class="text-center">
                    <h1 class="my-1 text-3xl font-semibold">Sign in</h1>
                    <p class="text-gray-500 dark:text-gray-400">Log in to gain access to the dashboard.</p>
                </div>
                <div class="m-7">
                    <form action="">
                        <div class="mb-6">
                            <label for="email" class="block mb-2 text-sm text-gray-600 dark:text-gray-400">Email
                                Address</label>
                            <input type="email" name="email" id="email" placeholder="Your email address"
                                class="w-full px-3 py-2 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-primary" />
                        </div>
                        <div class="mb-6">
                            <div class="flex justify-between mb-2">
                                <label for="password" class="text-sm text-gray-600 dark:text-gray-400">Password</label>
                                <a href="#!"
                                    class="text-sm text-gray-400 focus:outline-none focus:text-primary hover:text-primary dark:hover:text-indigo-300">Forgot
                                    password?</a>
                            </div>
                            <input type="password" name="password" id="password" placeholder="Your Password"
                                class="w-full px-3 py-2 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-primary" />
                        </div>
                        <div class="mb-6">
                            <button type="button"
                                class="w-full px-3 py-2 text-white bg-primary hover:bg-[#719af3] transition-all delay-100 ease-in-out rounded-md focus:bg-[#7399eb] focus:outline-none">Sign
                                in</button>
                        </div>
                </form>
            </div>
        </div>
    </div>
</div></template>