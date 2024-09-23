<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

use App\Http\Controllers\PostController;

// ルーティング
Route::middleware('api')->group(function () {
    # 投稿作成
    Route::post('/posts/create', [PostController::class, 'create']);
    # 投稿一覧表示
    Route::get('/posts', [PostController::class, 'index']);
    # 投稿表示
    Route::get('/posts/{id}', [PostController::class, 'show']);
    # 投稿編集
    Route::patch('/posts/update/{id}', [PostController::class, 'update']);
    # 投稿削除
    Route::delete('/posts/{id}', [PostController::class, 'delete']);
});
