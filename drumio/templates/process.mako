<%inherit file="layout.mako"/>
<div class="content">
  <h1><span class="font-semi-bold">Drumio</span></h1>
  <p class="lead">Welcome to <span class="font-normal">Drumio</span><br><span class="font-normal">an AI source separation engine</span>.</p>

  <form action="/store_track" method="post" accept_charset="utf-8" enctype="multipart/form-data">
    <div class="form-group">
      <label for="mp3"> Upload a Track</label>
      <input id="mp3" name="mp3" type="file" value="" class="form-control-file"/>
      <button type="submit">
        <span class="glyphicon glyphicon-open-file" aria-hidden="true">Upload</span>
      </button>
    </div>
  </form>

</div>
