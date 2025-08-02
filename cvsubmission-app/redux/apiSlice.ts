import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const baseAPI = 'http://127.0.0.1:8000';
export const apiSlice = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ 
    baseUrl: `${baseAPI}/api/`,
    prepareHeaders: (headers) => {
      console.log("🔍 Base URL used:", `${baseAPI}/api/`);
      return headers;
    },
  }),
  endpoints: (builder) => ({
    executeSubmission: builder.query<{ status: string }, void>({
      query: () => {
        const endpoint = 'execute_submission/';
        console.log("📡 API endpoint requested:", `${baseAPI}/api/${endpoint}`);
        return endpoint;
      },
    }),
  }),
});

export const { useLazyExecuteSubmissionQuery } = apiSlice;
