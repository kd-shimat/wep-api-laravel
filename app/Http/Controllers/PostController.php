<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Post;

class PostController extends Controller
{

 # 投稿作成
 public function create(Request $request)
 {
    // データを保存
    $post = Post::create([
        'title' => $request->input('title'),
        'content' => $request->input('content')
    ]);
    return response()->json(Post::all());
 }

    # 全件取得
  public function index()
  {
    $posts = Post::all();
    return response()->json($posts);
  }

  # 投稿表示
  public function show(Int $id)
  {
    $post = Post::find($id);
    return response()->json($post);
  }


  # 投稿編集
  public function update(Int $id, Request $request)
  {
    $post = Post::find($id);
    Post::update([
        'title' => $request->input('title'),
        'content' => $request->input('content')
    ]);
    return response()->json($post);
  }

  # 投稿削除
  public function delete(Int $id)
  {
    $post = Post::find($id)->delete();
    return response()->json(Post::all());
  }
}
