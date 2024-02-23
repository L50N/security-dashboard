<template>
    <div class="pt-12">
        <div>
            <div class="flex flex-row space-x-10">
                <div>
                <p>Configuration</p>
                <div class="text-2xl font-medium">
                    <p>wg0</p>
                </div>
            </div>

            <div>
                <p>Your distro</p>
                <div class="text-2xl font-medium">
                    <p>Debian 11 (Bullseye)</p>
                </div>
            </div>
            </div>
            <div class="flex flex-row space-x-12 py-8">
                <div>
                    <div class="flex flex-row space-x-[5px] items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-4">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z" />
                        </svg>
                        <p class="font-medium text-[18px] text-gray-800">Status</p>
                    </div>

                    <div class="flex items-center space-x-2">
                        <div class="bg-[#648de55d] h-3 w-3 rounded-full z-10 flex items-center justify-center">
                        </div>
                        <p class="text-gray-600">Active for <span class="font-medium underlin">2 days</span>.</p>
                    </div>
                </div>

                <div>
                    <div class="flex flex-row space-x-[5px] items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-4">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M10.5 19.5h3m-6.75 2.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-15a2.25 2.25 0 0 0-2.25-2.25H6.75A2.25 2.25 0 0 0 4.5 4.5v15a2.25 2.25 0 0 0 2.25 2.25Z" />
                        </svg>
                        <p class="font-medium text-[18px] text-gray-800">Connected devices</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">Currently <span class="font-medium underlin">3 devices</span> are
                            connected.</p>
                    </div>
                </div>

                <div>
                    <div class="flex flex-row space-x-[5px] items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-4">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M3 3v1.5M3 21v-6m0 0 2.77-.693a9 9 0 0 1 6.208.682l.108.054a9 9 0 0 0 6.086.71l3.114-.732a48.524 48.524 0 0 1-.005-10.499l-3.11.732a9 9 0 0 1-6.085-.711l-.108-.054a9 9 0 0 0-6.208-.682L3 4.5M3 15V4.5" />
                        </svg>
                        <p class="font-medium text-[18px] text-gray-800">Listen port</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">The current Wireguard port is <span
                                class="font-medium underlin">443</span>.</p>
                    </div>
                </div>

                <div>
                    <div class="flex flex-row space-x-[5px] items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="m20.893 13.393-1.135-1.135a2.252 2.252 0 0 1-.421-.585l-1.08-2.16a.414.414 0 0 0-.663-.107.827.827 0 0 1-.812.21l-1.273-.363a.89.89 0 0 0-.738 1.595l.587.39c.59.395.674 1.23.172 1.732l-.2.2c-.212.212-.33.498-.33.796v.41c0 .409-.11.809-.32 1.158l-1.315 2.191a2.11 2.11 0 0 1-1.81 1.025 1.055 1.055 0 0 1-1.055-1.055v-1.172c0-.92-.56-1.747-1.414-2.089l-.655-.261a2.25 2.25 0 0 1-1.383-2.46l.007-.042a2.25 2.25 0 0 1 .29-.787l.09-.15a2.25 2.25 0 0 1 2.37-1.048l1.178.236a1.125 1.125 0 0 0 1.302-.795l.208-.73a1.125 1.125 0 0 0-.578-1.315l-.665-.332-.091.091a2.25 2.25 0 0 1-1.591.659h-.18c-.249 0-.487.1-.662.274a.931.931 0 0 1-1.458-1.137l1.411-2.353a2.25 2.25 0 0 0 .286-.76m11.928 9.869A9 9 0 0 0 8.965 3.525m11.928 9.868A9 9 0 1 1 8.965 3.525" />
                        </svg>
                        <p class="font-medium text-[18px] text-gray-800">Listen adress</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">The list address is <span
                                class="font-medium underlin">10.66.66.1/24</span>.</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>